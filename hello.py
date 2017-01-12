#!/usr/bin/env python3

import os

from test_pb2 import Hello, World
from sync.server import Server

class Test:

    def hello(self, hello :Hello) -> World:
        return World(Message='Hello %s' % hello.Name)


if __name__ == "__main__":
    try:
        os.remove('/tmp/ascetic.socket')
    except:
        pass
    server= Server("/tmp/ascetic.socket")
    server.handlers = Test()
    server.serve()
