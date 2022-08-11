# part 1
with open("nameslist.txt") as f:
	for line in f:
		print(line)

# part 2
with open("nameslist.txt") as f:
	for line_number, line in enumerate(f):
		if line_number == 5:
			print(line)

# part 3
with open("nameslist.txt") as f:
	print(f.read(5))

# part 4 and 5
with open("nameslist.txt") as f:
	lines = f.readlines()
	lines = list(map(lambda line: line.rstrip(), lines))

	print(lines.count("Darth"))
	print(lines.count("Luke"))
	print(lines.count("Lea"))

# part 6
with open("nameslist.txt", "a+") as f:
	f.write("\nayal")

# part 7
lines = []
with open("nameslist.txt") as f:
	lines = f.readlines()
	lines = list(map(lambda line: line.rstrip(), lines))

with open("nameslist.txt", 'w') as f:
	for name in lines:
		if name == "Luke":
			name += " SkyWalker"

		f.write(name + "\n")

