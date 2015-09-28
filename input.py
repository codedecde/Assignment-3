f = open('input.txt')
counter = 0
rows=-1
cols=-1
num_cars = 0
car_pos = []
goal = ()
board = []
start_end_map = {}
for line in f:
	if(counter==0):
		line1 = line.split()
		rows = eval(line1[0])
		cols = eval(line1[1])
		board = [[0 for it in range(0,cols)] for it in range(0,rows)]
	elif(counter==1):
		num_cars = eval(line)
	else:
		dummy = line.split()
		if(len(dummy) == 5):
			element = [eval(dummy[0]),eval(dummy[1]),eval(dummy[3]) -1,eval(dummy[2]) - 1,dummy[4]]
			car_pos.append(element)
			if(dummy[4]=='H'):
				start = (element[2]*cols + element[3])
				end = start + element[1] - 1
				i = start
				while(i <= end):
					board[i/cols][i%cols] = element[0]
					i = i + 1
				start_end_map[element[0]] = (start,end)
			else:
				start = (element[2]*cols + element[3])
				end =  start + (element[1] - 1)*cols
				i = start
				while(i <= end):
					board[i/cols][i%cols] = element[0]
					i = i + cols
				start_end_map[element[0]] = (start,end)
		else:
			goal = (eval(dummy[1])-1,eval(dummy[0])-1)
	counter = counter + 1
empty_cells = []
#print start_end_map
for i in range(0,len(board)):
	for j in range(0,len(board[i])):
		#print str(board[i][j]),' ',
		if(board[i][j] ==0):
			empty_cells.append(i*cols + j)
	#print ''

f = open('problem_2.pddl','w')
f.write('(define (problem car_parking)\n(:domain car_park)\n(:objects ')
for i in range(1,num_cars+1):
	f.write('car-'+str(i)+' ')
f.write('\n\t')
for i in range(0,rows*cols):
	f.write('sq-'+str(i)+' ')
f.write(')\n')
f.write('(:init ')
for i in range(1,num_cars+1):
	f.write('(is_car car-'+str(i)+') ')
f.write('\n\t')
for  i in range(0,rows*cols):
	f.write('(is_board_pos sq-'+str(i)+') ')
f.write('\n\t')
for item in empty_cells:
	f.write('(is_empty sq-'+str(item)+') ')
f.write('\n\t')
for idx in start_end_map.keys():
	(start,end) = start_end_map[idx]
	f.write('(loc_car car-'+str(idx)+' sq-'+str(start)+' sq-'+str(end)+') ')
f.write('\n\t')
for row in range(0,rows):
	for col in range(1,cols):
		current_cell = (row*cols) + col
		prev_cell = (current_cell - 1)
		f.write('(left_adj sq-'+str(prev_cell)+' sq-'+str(current_cell)+') ')
f.write('\n\t')
for element in car_pos:
	if(element[4] == 'H'):
		f.write('(is_H car-'+str(element[0])+') ')
	else:
		f.write('(is_V car-'+str(element[0])+') ')
f.write('\n\t')
for row in range(0,rows):
	for col in range(0,cols-1):
		current_cell = (row*cols) + col
		next_cell = (current_cell  + 1)
		f.write('(right_adj sq-'+str(next_cell)+' sq-'+str(current_cell)+') ')
f.write('\n\t')
for row in range(1,rows):
	for col in range(0,cols):
		current_cell = (row*cols) + col
		prev_cell = ((row-1)*cols) + col
		f.write('(top_adj sq-'+str(prev_cell)+' sq-'+str(current_cell)+') ')
f.write('\n\t')
for row in range(0,rows-1):
	for col in range(0,cols):
		current_cell = (row*cols) + col
		next_cell = ((row+1)*cols) + col
		f.write('(bottom_adj sq-'+str(next_cell)+' sq-'+str(current_cell)+') ')
f.write(')\n')
f.write('(:goal ')

if(car_pos[0][4] == 'H'):
	(ga,gb) = goal
	if(gb <= car_pos[0][3]):
		start = ga*cols + gb
		end = start + car_pos[0][1] - 1
		f.write('(loc_car car-1 sq-'+str(start) + ' sq-' +str(end) +'))\n)')
	else:
		end = ga*cols + gb
		start = end - car_pos[0][1] + 1
		f.write('(loc_car car-1 sq-'+str(start) + ' sq-' +str(end) +'))\n)')		
else:
	(ga,gb) = goal
	if(ga <= car_pos[0][2]):
		start = ga*cols + gb
		end =  start + (car_pos[0][1] - 1)*cols
		f.write('(loc_car car-1 sq-'+str(start) + ' sq-' +str(end) +'))\n)')
	else:
		end = ga*cols + gb
		start = end - (car_pos[0][1] - 1)*cols
		f.write('(loc_car car-1 sq-'+str(start) + ' sq-' +str(end) +'))\n)')

