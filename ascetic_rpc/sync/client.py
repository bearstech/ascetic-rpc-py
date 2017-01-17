import socket
import functools
import logging

from ascetic_rpc.message_pb2 import Response, Request, Chunk
from .protocol import Protocol

logger = logging.getLogger(__name__)


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
        if not resp.Stream:
            r = response()
            r.ParseFromString(resp.RawOK)
            return r
        else:
            while True:
                chunk = self.protocol.read(Chunk)
                if chunk.HasField('Error'):
                    raise Exception(chunk.Error)
                if chunk.HasField('EOF'):
                    break
                r = response()
                r.ParseFromString(chunk.RawOK)
                yield r


class MockCall:
    def __init__(self, m, name):
        self._m = m
        self._name = name

    def __call__(self, arg):
        return self._m._client.Do(self._name, arg)


class Mock:
    def __init__(self, client):
        self._client = client

    def __get__(self, name):
        return MockCall(self, name)
