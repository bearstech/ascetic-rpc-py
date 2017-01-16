import struct
import inspect
import socket
import logging
import pdb
import time


from message_pb2 import Request, Response, Error, Chunk

logger = logging.getLogger(__name__)


class Server:

    def __init__(self, path, handlers):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.bind(path)
        #self.sock.settimeout(10)
        self.handlers = handlers

    def serve(self):
        self.sock.listen(0)
        while True:
            connection, client_address = self.sock.accept()
            self.handle_stream(connection, client_address)

    def handle_stream(self, connection, address):
        logger.debug("stream")
        #pdb.set_trace()
        while True:
            raw_size = connection.recv(2)
            logger.debug("Raw size %s" % raw_size)
            if raw_size == b'':
                connection.close()
                logger.warning("closing the socket")
                break
            size = struct.unpack("<h", raw_size)[0]
            logger.debug("Size: %i" % size)
            raw = connection.recv(size)
            print("Raw request ", raw)
            request = Request()
            request.ParseFromString(raw)
            logger.info(request)
            handler = getattr(self.handlers, request.Name)
            insp = inspect.getfullargspec(handler)
            req = insp.annotations[insp.args[1]]()
            req.ParseFromString(request.RawBody)
            err = None
            try:
                resp = handler(req)
            except Exception as e:
                err = Error(Message=str(e), Type=Error.APPLICATION)
            if err is not None:
                response(connection, Response(Error=err))
            else:
                if inspect.isgenerator(resp):
                    response(connection, Response(Stream=True))
                    try:
                        for r in resp:
                            response(connection,
                                     Chunk(RawOK=r.SerializeToString()))
                    except Exception as e:
                        err = Error(Message=str(e), Type=Error.APPLICATION)
                        response(connection, Chunk(Error=err))
                    response(connection, Chunk(EOF=True))
                else:
                    response(connection,
                             Response(RawOK=resp.SerializeToString()))

def response(connection, r):
    rawResp = r.SerializeToString()
    connection.sendall(struct.pack("<h", len(rawResp)))
    connection.sendall(rawResp)
