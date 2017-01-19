from asyncio import Protocol
import struct
import inspect

from ascetic_rpc.message_pb2 import Request, Response, Error, Chunk

SIZE = 1
BODY = 2


def write(wire, message):
    raw = message.SerializeToString()
    wire.write(struct.pack("<h", len(raw)))
    wire.write(raw)


class AsceticProtocol(Protocol):

    def __init__(self, handlers):
        self.handlers = handlers

    def connection_made(self, transport):
        self._transport = transport
        self._buffer = b''
        self._state = SIZE

    def data_received(self, data):
        self._buffer += data
        while True:
            if self._state == SIZE and len(self._buffer) >= 2:
                self._size = struct.unpack("<h", self._buffer[:2])[0]
                self._buffer = self._buffer[2:]
                self._state = BODY
            elif self._state == BODY and len(self._buffer) >= self._size:
                self.message_received(self._buffer[:self._size])
                self._buffer = self._buffer[self._size:]
                self._size = -1
                self._state = SIZE
            else:
                break

    def message_received(self, raw):
        request = Request()
        request.ParseFromString(raw)
        handler = getattr(self.handlers, request.Name)
        insp = inspect.getfullargspec(handler)
        req = insp.annotations[insp.args[1]]()
        req.ParseFromString(request.RawBody)
        r = handler(req)
        response = Response(RawOK=r.SerializeToString())
        write(self._transport, response)


class AsceticProtocolFactory:

    def __init__(self, handlers):
        self.handlers = handlers

    def __call__(self):
        return AsceticProtocol(self.handlers)



