#!/usr/bin/env python3

from asyncio import get_event_loop, start_unix_server, sleep
from test_pb2 import Hello, World

from ascetic_rpc.async.server import Server


class Test:

    async def mob(self, hello: Hello) -> World:
        for name in u"Eugesipe Adélard Ladislas".split(" "):
            await sleep(1)
            yield World(Message=name)

    async def hello(self, hello: Hello) -> World:
        print("hello ", hello)
        if hello.Name == "Adolf":
            raise Exception('Bad name')
        return World(Message='Hello %s' % hello.Name)


if __name__ == '__main__':
    loop = get_event_loop()
    server = Server(Test())
    coro = start_unix_server(server.make_handler,
                             path="/tmp/ascetic.socket", loop=loop)
    server = loop.run_until_complete(coro)
    loop.run_forever()
