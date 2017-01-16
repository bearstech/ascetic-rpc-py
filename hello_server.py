#!/usr/bin/env python3

import os
import logging

from test_pb2 import Hello, World
from ascetic_rpc.sync.server import Server

class Test:

    def mob(self, hello :Hello) -> World:
        for name in u"Eugesipe Adélard Ladislas".split(" "):
            yield World(Message=name)

    def hello(self, hello :Hello) -> World:
        print("hello ", hello)
        if hello.Name == "Adolph":
            raise Exception('Bad name')
        return World(Message='Hello %s' % hello.Name)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    try:
        os.remove('/tmp/ascetic.socket')
    except:
        pass
    server= Server("/tmp/ascetic.socket", Test())
    server.serve()
