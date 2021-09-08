import t1
import time
def GAME():
	stk=[]
	count = 0
	canvas_blank = '''
		|   |
	--------------
		|   |
	--------------
		|   |
	'''
	r='Y'
	b={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

	#player names
	p1=input('Enter player 1\'s name:')
	p2=input('Enter player 2\'s name:')
	print(p1,'is X and',p2,'will play with O')
	#intitial canvas
	print(b[1],'|',b[2],'|',b[3])
	print('-------------')
	print(b[4],'|',b[5],'|',b[6])
	print('----------------')
	print(b[7],'|',b[8],'|',b[9])
	print()
	#game logic
	w=False
	winner = ''
	while True:
		t1.x(b,stk)
		count+=1
		print()
		a=p1+'  Wins'
		o=p2+'  Wins'
		if b[1]==b[2]==b[3]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[4]==b[5]==b[6]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[7]==b[8]==b[9]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[1]==b[4]==b[7]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[2]==b[5]==b[8]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[3]==b[6]==b[9]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[1]==b[5]==b[9]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[3]==b[5]==b[7]=='X':
			print(a)
			winner = 'X'
			w='T'
		elif b[1]==b[2]==b[3]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[4]==b[5]==b[6]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[7]==b[8]==b[9]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[1]==b[4]==b[7]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[2]==b[5]==b[8]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[3]==b[6]==b[9]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[1]==b[5]==b[9]=='Y':
			print(o)
			winner = 'O'
			w='T'
		elif b[3]==b[5]==b[7]=='Y':
			print(o)
			winner = 'O'
			w='T'
		if w=='T':
			break
		t1.o(b,stk)
		count+=1
		print()
	
	# winner logic goes into the text input file
	file = open('score.txt', 'a')
	# file opened in append mode
	write_head = ('Game played between' + ' ' + str(p1) + ' and ' + str(p2) +
	'\nOn time: ' + str(time.strftime('%H')) + ':' + str(time.strftime('%M')) +
	str(time.strftime('%S')) + '\nOn date: ' + str(time.strftime('%d')) + '/' +
	str(time.strftime('%m')) + '/' + str(time.strftime('%y')))
	if winner == 'X':
		write_head += '\n' + p1 + ' wins\n\n'
	elif winner == 'O':
		write_head += '\n' + p2 + ' wins\n\n'
	file.write(write_head)
	file.close()