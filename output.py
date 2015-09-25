fin = open('problem.plan')
fout = open('output.txt', 'w')



for line in fin:
	if (bool('Plan length: ' in line)):
		line = line.split()
		fout.write(str(line[2])+'\n')

fin = open('problem.plan')

for line in fin:
	if (bool('move_' in line)):
		print('hello\n')
		line = line.split('-')
		fout.write(line[1][0] + ' ')
		line = line[0].split('_')
		fout.write(str(line[1][0]).upper() + ' 1\n')


