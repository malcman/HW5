import re
mysum = 0
with open("SampleData.txt", "r") as f:
	for num in re.findall('[0-9]+', f.read()):
		mysum += int(num)
print(mysum)