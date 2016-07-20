#file = open("recursive_list_pop.txt", "w")

#note: this function goes from 100 to 1, recursively, so in comparison to 
# the loop solution it is in reverse order, the print out. 


def recurse_printer(n):
	if n < 3:
		return
	elif n % 3 == 0 and n % 5 != 0:
		print "Crackle"
		file.write("Crackle")
		file.write('\n')
		recurse_printer(n-1)
	elif n % 5 == 0 and n % 3 != 0:
		print "Pop"
		file.write("Pop")
		file.write('\n')
		recurse_printer(n-1)
	elif n % 5 == 0 and n % 3 == 0:
		print "CracklePop"
		file.write("CracklePop")
		file.write('\n')
		recurse_printer(n-1)
	elif n > 3:
		print n
		file.write('%d' % n)
		recurse_printer(n-1)

recurse_printer(100)
#file.close()



