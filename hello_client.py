#!/usr/bin/env python3

import sys

from test_pb2 import Hello, World
from sync.client import Client

client = Client("/tmp/ascetic.socket")

print(client.do("hello", Hello(Name=sys.argv[1]), World).Message)
