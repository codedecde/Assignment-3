fin = open('problem.plan')
fout = open('output.txt', 'w')

number_of_steps = 0
for line in fin:
	if (bool('Plan length: ' in line)):
		line = line.split()
		number_of_steps = eval(line[2])
fin.close()

fin = open('problem.plan')

counter = 0
all_moves = []
moves = []
current_car = prev_car = '' 
for line in fin:
	if (bool('move_' in line)):
		#if ( counter == 0):
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
			#counter = counter + 1
'''else:
			line1 = line.split('-')
			if ( line1[0] == templine[0] and line1[1][0] == templine[1][0] ):
				counter = counter + 1
				print('helo\n')
			else:
				printline = templine
				fout.write(printline[1][0] + ' ')
				printline = printline[0].split('_')
				fout.write(str(printline[1][0]).upper() + ' ' + str(counter) + '\n')
				templine = line.split('-')
				counter = 1

fout.write(templine[1][0] + ' ')
templine = templine[0].split('_')
fout.write(str(templine[1][0]).upper() + ' ' + str(counter) + '\n')'''