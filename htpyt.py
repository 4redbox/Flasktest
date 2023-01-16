#python code for odd and even split

def split(mix):
	evenli = []
	oddli  = []
	
	for i in mix:
		if (i % 2 == 0):
			evenli.append(i)
		else:
			oddli.append(i)
	print("Even Lists:", evenli)	
	print("Odd Lists: ", oddli)

mix = [1,2,3,4,5,8,3]
split(mix)
