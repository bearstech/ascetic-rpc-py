#!/usr/bin/env python3

import sys
import logging

from test_pb2 import Hello, World
from sync.client import Client

logging.basicConfig(level=logging.DEBUG)

client = Client("/tmp/ascetic.socket")

name = sys.argv[1]
hello = Hello(Name=name)
print("hello ", hello)

if name != "Pacome":
    world = client.do("hello", hello, World)
    print("world ", world)
    print(world.Message)
else:
    worlds = client.do("mob", hello, World)
    for world in worlds:
        print(world.Message)
