import sys

personName = sys.argv[1]
attribute = sys.argv[2]

print "Hello " + personName + ", you are " + attribute + "!"

timesTable = int(sys.argv[3])
for i in range(1,20):
	print timesTable*i
