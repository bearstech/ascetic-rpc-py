import struct
import inspect

from ascetic_rpc.message_pb2 import Request, Response, Error, Chunk

SIZE = 1
BODY = 2


def write(wire, message):
    raw = message.SerializeToString()
    wire.write(struct.pack("<h", len(raw)))
    wire.write(raw)


class Server:

    def __init__(self, handlers):
        self.handlers = handlers

    async def cb(self, reader, writer):
        rawsize = await reader.readexactly(2)
        size = struct.unpack("<h", rawsize)[0]
        raw = await reader.readexactly(size)
        request = Request()
        request.ParseFromString(raw)
        handler = getattr(self.handlers, request.Name)
        insp = inspect.getfullargspec(handler)
        req = insp.annotations[insp.args[1]]()
        req.ParseFromString(request.RawBody)
        r = await handler(req)
        response = Response(RawOK=r.SerializeToString())
        write(writer, response)

