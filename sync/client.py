import socket
import functools
import struct

from message_pb2 import Response, Request


class Client:
    def __init__(self, path):
        self._path = path
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(path)

    def do(self, name, arg, response):
        req = Request(Name=name, RawBody=arg.SerializeToString()).SerializeToString()
        self.sock.sendall(struct.pack("<h", len(req)))
        self.sock.sendall(req)
        rsize = struct.unpack("<h", self.sock.recv(2))[0]
        resp = Response()
        resp.ParseFromString(self.sock.recv(rsize))
        r = response()
        r.ParseFromString(resp.RawOK)
        return r


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
