#!/usr/bin/env python3

import os

from test_pb2 import Hello, World
from sync.server import Server

class Test:

    def hello(self, hello :Hello) -> World:
        if hello.Name == "Adolph":
            raise Exception('Bad name')
        if hello.Name == "Pacome":
            for name in u"Eugesipe Adélard Ladislas".split(" "):
                yield World(Message=name)
        return World(Message='Hello %s' % hello.Name)


if __name__ == "__main__":
    try:
        os.remove('/tmp/ascetic.socket')
    except:
        pass
    server= Server("/tmp/ascetic.socket", Test())
    server.serve()
