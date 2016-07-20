file = open("recurse_list.txt", "w")
number_file = open("number_list.txt", "w")

for i in range(1,101):
	number_file.write('%d' % i)
	number_file.write('\n')
number_file.close()

for i in range(1,101):
	#check if it is divisible only by 3 
	if i % 3 == 0 and i % 5 != 0:
		#print "Crackle"
		file.write("Crackle")
		file.write('\n')
	#check if it is divisible only by 5
	elif i % 5 == 0 and i % 3 != 0:
		#print "Pop"
		file.write("Pop")
		file.write('\n')
	#check if it is divisible by 3 and 5
	elif i % 3 == 0 and i % 5 ==0:
		#print "CracklePop"
		file.write("CracklePop")
		file.write('\n')
	elif i % 3 != 0 and i %5 != 0:
		#print i
		file.write('%d' % i)
		file.write('\n')


file.close()
