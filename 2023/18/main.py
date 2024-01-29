# import re
# R"([RULD]) (\d+) \(#([a-f0-9]{6})\)"

complex_d = {"R": 1, "D": 1j, "L": -1, "U": -1j}
plan = list(map(str.split, open("data.txt")))


# There's a much nicer way to do this with maths, but I didn't see it at the time
# Basically, if you use Green's theorem with the inputs you only get the area
# contained within the centres of the grid cells on the loop. I adjusted for this
# by calculating where the actual vertices on the outside would be, and plugging
# them into Green's theorem instead. This is unnecessary, as the amount of area you
# miss by just using the inputs is a known quantity: A_extra = 0.5 for each cell on the
# perimeter + 0.25 for each convex corner - 0.25 for each concave corner
# As the shape is a closed loop there are always four more convex corners than
# concave corners, so A_extra = perimeter/2 + 1
def create_verts(_plan):
    verts_ri = [0]
    verts_li = [0]
    for i, (direction, distance) in enumerate(_plan):
        next_d, _ = _plan[(i + 1) % len(_plan)]
        prev_d, _ = _plan[(i - 1) % len(_plan)]

        offset = int(direction * 1j == next_d) + int(prev_d * 1j == direction) - 1
        verts_ri.append(verts_ri[-1] + direction * (distance + offset))
        verts_li.append(verts_li[-1] + direction * (distance - offset))
    return verts_ri, verts_li


def greens_theorem(verts):
    area = 0
    prev_v = verts[0]
    for v in verts[1:]:
        dv = v - prev_v
        area += prev_v.real * dv.imag
        prev_v = v
    return area


answer1 = max(
    map(
    	greens_theorem, 
    	create_verts([(complex_d[d], int(s)) for d,s,_ in plan])
    )
)
answer2 = max(
    map(
        greens_theorem,
        create_verts([(complex_d["RDLU"[int(c[-2])]], int(c[2:-2], 16)) for _,_,c in plan]),
    )
)

print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert answer1 == 49897
assert answer2 == 194033958221830
