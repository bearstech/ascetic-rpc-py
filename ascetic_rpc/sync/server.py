import struct
import inspect
import socket
import logging
import time


from ascetic_rpc.message_pb2 import Request, Response, Error, Chunk
from .protocol import Protocol


logger = logging.getLogger(__name__)


class Server:

    def __init__(self, path, handlers):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.bind(path)
        self.handlers = handlers

    def serve(self):
        self.sock.listen(0)
        while True:
            connection, client_address = self.sock.accept()
            self.handle_stream(connection, client_address)

    def handle_stream(self, connection, address):
        protocol = Protocol(connection)
        while True:
            try:
                request = protocol.read(Request)
            except StopIteration:
                break
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
                protocol.write(Response(Error=err))
            else:
                if inspect.isgenerator(resp):
                    protocol.write(Response(Stream=True))
                    try:
                        for r in resp:
                            protocol.write(Chunk(RawOK=r.SerializeToString()))
                    except Exception as e:
                        err = Error(Message=str(e), Type=Error.APPLICATION)
                        protocol.write(Chunk(Error=err))
                    protocol.write(Chunk(EOF=True))
                else:
                    protocol.write(Response(RawOK=resp.SerializeToString()))
