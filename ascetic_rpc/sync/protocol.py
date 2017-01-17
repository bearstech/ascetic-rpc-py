import struct


class Protocol:
    def __init__(self, wire):
        self.wire = wire

    def write(self, message):
        raw = message.SerializeToString()
        self.wire.sendall(struct.pack("<h", len(raw)))
        self.wire.sendall(raw)

    def read(self, model):
        size = struct.unpack("<h", self.wire.recv(2))[0]
        m = model()
        m.ParseFromString(self.wire.recv(size))
        return m
