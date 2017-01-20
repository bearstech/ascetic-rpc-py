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

    async def make_handler(self, reader, writer):
        request = Request()
        request.ParseFromString(await read(reader))

        handler = getattr(self.handlers, request.Name)
        insp = inspect.getfullargspec(handler)
        req = insp.annotations[insp.args[1]]()
        req.ParseFromString(request.RawBody)

        if inspect.isasyncgenfunction(handler):
            write(writer, Response(Stream=True))
            try:
                async for r in handler(req):
                    write(writer, Chunk(RawOK=r.SerializeToString()))

            except Exception as e:
                err = Error(Message=str(e), Type=Error.APPLICATION)
                write(writer, Chunk(Error=err))

            write(writer, Chunk(EOF=True))

        else:
            assert inspect.iscoroutinefunction(handler)
            try:
                resp = await handler(req)

            except Exception as e:
                err = Error(Message=str(e), Type=Error.APPLICATION)
                write(writer, Response(Error=err))
            else:
                write(writer, Response(RawOK=resp.SerializeToString()))
