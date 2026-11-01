"""Generate icon-180.png and icon-512.png (black dumbbell on yellow background) with the standard library only."""
import struct
import zlib
from pathlib import Path

BG = (255, 225, 77)
FG = (0, 0, 0)

# Shapes in a 0..1 unit square: (x0, y0, x1, y1, corner radius)
RECTS = [
    (0.14, 0.34, 0.24, 0.66, 0.03),  # outer plate left
    (0.24, 0.27, 0.34, 0.73, 0.03),  # inner plate left
    (0.66, 0.27, 0.76, 0.73, 0.03),  # inner plate right
    (0.76, 0.34, 0.86, 0.66, 0.03),  # outer plate right
    (0.34, 0.465, 0.66, 0.535, 0.02),  # bar
]


def inside(x, y):
    for x0, y0, x1, y1, r in RECTS:
        if x0 <= x <= x1 and y0 <= y <= y1:
            cx = min(max(x, x0 + r), x1 - r)
            cy = min(max(y, y0 + r), y1 - r)
            if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                return True
    return False


def make(size, path):
    ss = 3  # supersampling for smooth edges
    rows = []
    for py in range(size):
        row = bytearray([0])
        for px in range(size):
            hits = sum(inside((px + (i + .5) / ss) / size, (py + (j + .5) / ss) / size)
                       for i in range(ss) for j in range(ss)) / (ss * ss)
            row += bytes(round(BG[c] + (FG[c] - BG[c]) * hits) for c in range(3))
        rows.append(bytes(row))
    raw = zlib.compress(b''.join(rows), 9)

    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) + chunk(b'IDAT', raw) + chunk(b'IEND', b'')
    Path(path).write_bytes(png)


if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent
    make(180, root / 'icon-180.png')
    make(512, root / 'icon-512.png')
    print('ok')
