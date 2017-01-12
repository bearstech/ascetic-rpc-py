import struct
import inspect
import socket

from message_pb2 import Request, Response, Error


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
            except e:
                err = Error(Message=str(e), Type=Error.APPLICATION)
            if err is None:
                rawResp = Response(RawOK=resp.SerializeToString()).SerializeToString()
            else:
                rawResp = Response(Error=err).SerializeToString()
            connection.sendall(struct.pack("<h", len(rawResp)))
            connection.sendall(rawResp)

