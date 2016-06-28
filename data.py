import sys

# define function to test if arg is integer
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

status = sys.argv[1]

f = open("data.csv","r")
#print(f)

cost = 0
paid = 0
balance = 0
f.seek(0) #put cursor back to start of file f
print "Clients with status = " + status
statusCount = 0
for line in f:
    line = line.strip("\n").strip("\r") #cleans off spurious carriage returns aka new line character
    entry = line.split(",") # split line at each comma, into arrays 
    if RepresentsInt(entry[2]):
        cost += int(entry[2])
    if RepresentsInt(entry[3]):
        paid += int(entry[3])
    if RepresentsInt(entry[4]):
        balance += int(entry[4])
    if entry[5]==status:
        print entry[1]
        statusCount += 1

print "There are " + str(statusCount) + " clients with " + status + " accounts"
print "Total cost = " + str(cost)
print "Total paid = " + str(paid)
print "Total balance = " + str(balance)




f.close()
