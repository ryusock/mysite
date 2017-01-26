#f = open('crowd-estimates.csv')
#contents = f.read()
#f.close()
#new_contents = contents.replace('\n', ',')
#f = open('crowd-estimates.txt', 'w')
#f.write(new_contents)
#f.close()

f = open('crowd-estimates.csv')
contents = f.read()
f.close()
newcontents = ""

lines = contents.split("\n")
for l in lines:
	index = l.find("US")
	counts = l[index + 3:]
	if (counts != ","):
		if counts.find("\"") >= 0:
			counts = counts.replace(",\"", " ")
			counts = counts.replace("\"", "")
			counts = counts.replace(",", "")
			counts = counts.replace(" ", ",")
			l = l[:index+3] + counts
		newcontents = newcontents + l + "\n"

f = open('crowd-estimates.txt', 'w')
f.write(newcontents)
f.close()
