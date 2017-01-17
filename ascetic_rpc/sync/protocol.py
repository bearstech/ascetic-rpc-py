import struct


class Protocol:
    def __init__(self, wire):
        self.wire = wire

    def write(self, message):
        raw = message.SerializeToString()
        self.wire.sendall(struct.pack("<h", len(raw)))
        self.wire.sendall(raw)

    def read(self, model):
        raw = self.wire.recv(2)
        if raw == b'':
            raise StopIteration
        size = struct.unpack("<h", raw)[0]
        m = model()
        m.ParseFromString(self.wire.recv(size))
        return m
