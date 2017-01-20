import struct
import inspect

from ascetic_rpc.message_pb2 import Request, Response, Error, Chunk


def write(wire, message):
    raw = message.SerializeToString()
    wire.write(struct.pack("<h", len(raw)))
    wire.write(raw)


async def read(wire):
    rawsize = await wire.readexactly(2)
    size = struct.unpack("<h", rawsize)[0]
    return await wire.readexactly(size)


class Server:

    def __init__(self, handlers):
        self.handlers = handlers

    async def cb(self, reader, writer):
        request = Request()
        request.ParseFromString(await read(reader))
        handler = getattr(self.handlers, request.Name)
        insp = inspect.getfullargspec(handler)
        req = insp.annotations[insp.args[1]]()
        req.ParseFromString(request.RawBody)
        r = await handler(req)
        response = Response(RawOK=r.SerializeToString())
        write(writer, response)
