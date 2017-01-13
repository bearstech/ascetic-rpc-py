import struct
import inspect
import socket

from message_pb2 import Request, Response, Error, Stream, Chunk, EOF


class Server:

    def __init__(self, path, handlers):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.bind(path)
        self.handlers = handlers

    def serve(self):
        self.sock.listen(1)
        while True:
            connection, client_address = self.sock.accept()
            self.handle_stream(connection, client_address)

    def handle_stream(self, connection, address):
        while True:
            raw_size = connection.recv(2)
            if raw_size == b'':
                connection.close()
                break
            size = struct.unpack("<h", raw_size)[0]
            raw = connection.recv(size)
            request = Request()
            request.ParseFromString(raw)
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
                    response(connection, Response(Stream=Stream()))
                    try:
                        for r in resp:
                            print("r", type(r), r)
                            response(connection,
                                     Chunk(RawOK=r.SerializeToString()))
                    except Exception as e:
                        err = Error(Message=str(e), Type=Error.APPLICATION)
                        response(connection, Chunk(Error=err))
                    response(connection, Chunk(EOF=EOF()))
                else:
                    response(connection,
                             Response(RawOK=resp.SerializeToString()))

def response(connection, r):
    rawResp = r.SerializeToString()
    connection.sendall(struct.pack("<h", len(rawResp)))
    connection.sendall(rawResp)
