import re
import math

_workflows, _parts = open("data.txt").read().split("\n\n")

workflows = {}
for w in _workflows.split("\n"):
	name, *rules, default = re.findall(R"(?:([xmas])([<>])(\d+):(\w+))|(\w+)", w)
	workflows[name[-1]] = (*rules, (default[-1],))

parts = [
	list(map(int, p[:-1].replace("=", ",").split(",")[1::2]))
	for p in _parts.split("\n")
]


def apply(w, p):
	for r in w:
		if len(r) == 1:
			return r[0]
		elif (p["xmas".index(r[0])] < int(r[2])) == (r[1] == "<"):
			return r[3]


answer1 = 0
for p in parts:
	destination = "in"
	while destination not in ["A", "R"]:
		destination = apply(workflows[destination], p)
	if destination == "A":
		answer1 += sum(p)

def apply_ranges(w, p):
	results = []
	for c, *cs in w:
		if not cs:
			results.append((c, p))
		else:
			p0, pf, p1 = p[c][0], int(cs[1]), p[c][1]
			np = {k: [a,b] for k,(a,b) in p.items()}
			if cs[0] == "<" and p0 < pf:
				np[c][1] = min(p1, pf - 1)
				p[c][0] = np[c][1] + 1
				results.append((cs[2], np))
			elif cs[0] == ">" and p1 > pf:
				np[c][0] = max(p0, pf + 1)
				p[c][1] = np[c][0] - 1
				results.append((cs[2], np))
			if p[c][1] < p[c][0]:
				break
	return results


ranges = [("in", {c: [1,4000] for c in "xmas"})]
answer2 = 0
while ranges:
	r = ranges.pop()
	if r[0] == "A":
		answer2 += math.prod(b - a + 1 for a, b in r[1].values())
	elif r[0] != "R":
		ranges.extend(apply_ranges(workflows[r[0]], r[1]))


print(f"Part one: {answer1}")
print(f"Part two: {answer2}")

assert answer1 == 350678
assert answer2 == 124831893423809
