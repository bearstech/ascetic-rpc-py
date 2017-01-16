import socket
import functools
import struct
import logging

from ascetic_rpc.message_pb2 import Response, Request, Chunk

logger = logging.getLogger(__name__)


class Client:

    def __init__(self, path):
        self._path = path
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(path)

    def do(self, name, arg, response):
        print("do", name, arg, response)
        logger.debug(name, arg)
        req = Request(Name=name,
                      RawBody=arg.SerializeToString()).SerializeToString()
        print("req", req)
        self.sock.sendall(struct.pack("<h", len(req)))
        self.sock.sendall(req)
        rsize = struct.unpack("<h", self.sock.recv(2))[0]
        resp = Response()
        resp.ParseFromString(self.sock.recv(rsize))
        logger.debug("resp isTstream %s" % str(resp.Stream))
        if resp.HasField('Error'):
            raise Exception(resp.Error)
        if not resp.Stream:
            r = response()
            r.ParseFromString(resp.RawOK)
            return r
        else:
            while True:
                csize = struct.unpack("<h", self.sock.recv(2))[0]
                chunk = Chunk()
                chunk.ParseFromString(self.sock.recv(csize))
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
