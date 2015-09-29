import sys
problem_file = ''
output_file = ''
if(len(sys.argv > 1)):	
	problem_file = sys.argv[1] + '.plan'
	output_file = sys.argv[1] + '.out'

fin = open(problem_file)
fout = open(output_file, 'w')


all_moves = []
moves = []
buffer  = []


for line in fin:
	if (bool('move_' in line)):
		buffer.append(line)

if (len(buffer) == 0):
	fout.write('-1')
else:
	visited = set()
	car_data = {}
	#car_data = { 1:[lenght,start_pos,flag] }
	col = -1
	for line in buffer:
		line = line.split()
		if (not line[1] in visited):
			visited.add(line[1])
			list_Item = [0,0,'']
			if(line[0] == 'move_left' or line[0] == 'move_right'):
				list_Item[2] = 'H'
				list_Item[0] = abs(eval(line[2].lstrip('sq-')) - eval(line[3].lstrip('sq-'))) + 1
				list_Item[1] = eval(line[2].lstrip('sq-'))
				car_data[line[1]] = []
				for item in list_Item:
					car_data[line[1]].append(item)
			else:
				col = abs(eval(line[2].lstrip('sq-')) - eval(line[4].lstrip('sq-')))
				list_Item[2] = 'V'
				list_Item[0] = (abs(eval(line[2].lstrip('sq-')) - eval(line[3].lstrip('sq-'))) / col ) + 1
				list_Item[1] = eval(line[2].lstrip('sq-'))
				car_data[line[1]] = []
				for item in list_Item:
					car_data[line[1]].append(item)

	occupied = []
	for item in car_data.keys():
		if ( car_data[item][2] == 'H'):
			for i in range(0, car_data[item][0]):
				occupied.append(car_data[item][1] + i)
		elif ( car_data[item][2] == 'V'):
			for i in range(0, car_data[item][0]):
				occupied.append(car_data[item][1] + (i*col))
	temp_buffer = []
	counter = 1
	current_car = prev_car = ''
	found_at = -1
	temp_occupied = []
	for i in range(0, len(buffer)):
		for item in occupied:
			temp_occupied.append(item)
		temp_car_data = car_data.copy()
		#print car_data
		prev_car = buffer[i].split()[1]
		for j in range (0, len(buffer)):
			if ( j <= i ):
				temp_buffer.append(buffer[j])
				#print (temp_buffer[j])
			else:
				current_car = buffer[j].split()[1]
				if(current_car == prev_car):
					temp_buffer.insert(counter, buffer[j])
					found_at = j
					break
				else:
					temp_buffer.append(buffer[j])
		valid = 1
		#print temp_buffer
		#print ('\n')
		for j in range(0, len(temp_buffer)):
			move_car = temp_buffer[j].split()[1]
			carpos = temp_buffer[j].split('-')[2]
			carpos = carpos.split()[0]
			car_pos = eval(carpos)
			#print temp_buffer[j]
			#print temp_occupied
			#print car_pos
			#car_pos = car_pos1.split()[0]
			direction = temp_buffer[j].split('_')[1][0]
			if ( direction == 'r' and (not (car_pos + car_data[move_car][0]) in temp_occupied)):
				temp_occupied.append(car_pos + car_data[move_car][0])
				temp_occupied.remove(car_pos)
			elif ( direction == 'l' and (not (car_pos - 1) in temp_occupied)):
				temp_occupied.append(car_pos  - 1)
				temp_occupied.remove(car_pos + car_data[move_car][0] - 1)
			elif ( direction == 'd' and (not (car_pos + col*car_data[move_car][0]) in temp_occupied)):
				temp_occupied.append(car_pos + col*car_data[move_car][0])
				temp_occupied.remove(car_pos)
			elif ( direction == 'u' and (not (car_pos - col) in temp_occupied)):
				temp_occupied.append(car_pos - col)
				temp_occupied.remove(car_pos + col*(car_data[move_car][0]-1))
			else:
				valid = 0
				break
		#print ('valid = ' + str(valid) + '\n' )
		if (valid == 1 and found_at != -1 ):
			buffer.insert(i + 1, buffer[found_at])
			del buffer[j+1]
		temp_buffer = []
		temp_occupied=[]
		found_at = -1
		counter = counter + 1


	for line in buffer:
		current_car = line.split()[1]
		if(current_car == prev_car):
			moves.append(line)
		else:
			prev_car = current_car
			if(len(moves) != 0):
				all_moves.append(moves)
			moves = []
			moves.append(line)
	all_moves.append(moves)

	fout.write(str(len(all_moves)) + '\n')

	for lines in all_moves:
		line = lines[0]
		line = line.split('-')
		fout.write(line[1][0] + ' ')
		line = line[0].split('_')	
		fout.write(str(line[1][0]).upper() + ' ' + str(len(lines)) + '\n')
			