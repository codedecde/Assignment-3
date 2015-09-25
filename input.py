f = open('input.txt')
counter = 0
rows=-1
cols=-1
num_cars = 0
car_pos = []
goal = ()
for line in f:
	if(counter==0):
		line1 = line.split()
		rows = eval(line1[0])
		cols = eval(line1[1])
	elif(counter==1):
		num_cars = eval(line)
	else:
		dummy = line.split()
		if(len(dummy) == 5):
			element = [eval(dummy[0]),eval(dummy[1]),eval(dummy[2]),eval(dummy[3]),dummy[4]]
		else:
			goal = (eval(dummy[0]),eval(dummy[1]))
		car_pos.append(element)
	counter = counter + 1

print car_pos,goal

