# print error if array is empty except for name
# mean.py

# use sys package for this program
import sys

#initialize var to 0
sum = 0

# chk length of input to ensure not 0
if len(sys.argv) == 1:
	print 'Error: No arguments given.'
	sys.exit()
#average numbers in the series
for num in sys.argv[1:]:
    sum += float(num)
print sum / (len(sys.argv) - 1)
