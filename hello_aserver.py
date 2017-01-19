#!/usr/bin/env python3

from asyncio import get_event_loop
from test_pb2 import Hello, World

from ascetic_rpc.async.server import AsceticProtocolFactory


class Test:

    def mob(self, hello: Hello) -> World:
        for name in u"Eugesipe Adélard Ladislas".split(" "):
            yield World(Message=name)

    def hello(self, hello: Hello) -> World:
        print("hello ", hello)
        if hello.Name == "Adolf":
            raise Exception('Bad name')
        return World(Message='Hello %s' % hello.Name)


if __name__ == '__main__':
    loop = get_event_loop()
    coro = loop.create_unix_server(AsceticProtocolFactory(Test()),
                                   "/tmp/ascetic.socket")
    server = loop.run_until_complete(coro)
    loop.run_forever()
