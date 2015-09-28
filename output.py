fin = open('problem.plan')
#fout = open('output.txt', 'w')

counter = 0
all_moves = []
moves = []
buffer  = []

for line in fin:
	if (bool('move_' in line)):
		buffer.append(line)

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

for item in car_data.keys():
	print item, car_data[item]

current_car = prev_car = '' 

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
			