#!/usr/bin/env python3

import sys
import logging

from test_pb2 import Hello, World
from ascetic_rpc.sync.client import Client

logging.basicConfig(level=logging.DEBUG)

client = Client("/tmp/ascetic.socket")

name = sys.argv[1]
hello = Hello(Name=name)

if name == "Pacome":
    worlds = client.do("mob", hello, World)
    for world in worlds:
        print(world.Message)
else:
    world = client.do("hello", hello, World)
    print(world.Message)
