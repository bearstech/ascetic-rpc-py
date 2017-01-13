#!/usr/bin/env python3

import sys

from test_pb2 import Hello, World
from sync.client import Client

client = Client("/tmp/ascetic.socket")

name = sys.argv[1]
if name != "Pacome":
    print(client.do("hello", Hello(Name=name), World).Message)
else:
    for world in client.do("hello", Hello(Name=name), World):
        print(world.Message)
