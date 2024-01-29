import functools

modules = {}

def parse():
	for line in open("data.txt"):
		line = line.replace(",", " ").split()
		module = ["", "", line[2:]]
		if line[0] == "broadcaster":
			modules["broadcaster"] = [line[2:], "broadcaster"]
		elif line[0][0] in "%&":
			mod_type = line[0][0]
			mod_name = line[0][1:]
			mod_outs = line[2:]
			mod_state = 0 if mod_type == "%" else {}
			modules[mod_name] = [mod_outs, mod_type, mod_state]
		else:
			print(line)
			assert 0


def connect_inputs():
	for k, v in modules.items():
		for d in v[0]:
			if d in modules:
				if modules[d][1] == "&":
					modules[d][2][k] = 0


parse()
connect_inputs()

def push_button(i):
	global xm_on
	pulses = [("broadcaster", 0, "button")]
	n_pulses = [1,0]
	while pulses:
		p = pulses.pop(0)
		#print(f"{p[2]} -{"high" if p[1] else "low"}-> {p[0]}")
		if(p[2] == "xm" and p[1]):
			print("xm sent high during", i+1)
		if(p[2] == "hz" and p[1]):
			print("hz sent high during", i+1)
		if(p[2] == "qh" and p[1]):
			print("qh sent high during", i+1)
		if(p[2] == "pv" and p[1]):
			print("pv sent high during", i+1)
		module = modules[p[0]]
		if module[1] == "broadcaster":
			for t in module[0]:
				pulses.append((t, p[1], p[0]))
				n_pulses[pulses[-1][1]] += 1
		elif module[1] == "%" and not p[1]:
			modules[p[0]][2] = int(not modules[p[0]][2])
			for t in module[0]:
				pulses.append((t, modules[p[0]][2], p[0]))
				n_pulses[pulses[-1][1]] += 1
		elif module[1] == "&":
			modules[p[0]][2][p[2]] = p[1]
			for t in module[0]:
				pulses.append((t, int(not all(modules[p[0]][2].values())), p[0]))
				n_pulses[pulses[-1][1]] += 1

	return n_pulses

modules['rx'] = [[], "output", 0]
low,high = 0,0
for i in range(10000):
	np = push_button(i)
	low += np[0]
	high += np[1]
print(low*high)
