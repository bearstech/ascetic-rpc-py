import socket
import logging

from ascetic_rpc.message_pb2 import Response, Request, Chunk
from .protocol import Protocol

logger = logging.getLogger(__name__)


class Streamer:

    def __init__(self, protocol, model):
        self.protocol = protocol
        self.model = model

    def __iter__(self):
        return self

    def __next__(self):
        chunk = self.protocol.read(Chunk)
        if chunk.HasField('Error'):
            raise Exception(chunk.Error)
        if chunk.HasField('EOF'):
            raise StopIteration
        r = self.model()
        r.ParseFromString(chunk.RawOK)
        return r


class Client:

    def __init__(self, path):
        self._path = path
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(path)
        self.protocol = Protocol(sock)

    def do(self, name, arg, response):
        req = Request(Name=name,
                      RawBody=arg.SerializeToString())
        self.protocol.write(req)
        resp = self.protocol.read(Response)
        if resp.HasField('Error'):
            raise Exception(resp.Error)
        if resp.Stream:
            return Streamer(self.protocol, response)
        r = response()
        r.ParseFromString(resp.RawOK)
        return r
