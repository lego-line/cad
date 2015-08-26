#! python3

import fileinput
import sys

seen = set()

for line in fileinput.input(inplace=True):
	if line.startswith("1 "):
		if line in seen:
			print("Found {!r} duplicated".format(line), file=sys.stderr)
			continue
	
		seen.add(line)

	sys.stdout.write(line)