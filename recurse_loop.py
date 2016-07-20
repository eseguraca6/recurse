#this is the actual solution submitted for the recurse center application

for i in range(1,101):
	#check if it is divisible only by 3 
	if i % 3 == 0 and i % 5 != 0:
		print "Crackle"
	#check if it is divisible only by 5
	elif i % 5 == 0 and i % 3 != 0:
		print "Pop"
	#check if it is divisible by 3 and 5
	elif i % 3 == 0 and i % 5 ==0:
		print "CracklePop"

