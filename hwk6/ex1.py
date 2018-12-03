from __future__ import print_function
import random as rand

#variables pertinent per run
real_position = 0 # assert the starting pos is always 0
observation = False

#prior
x = [.1] * 10

#actuation model
xtut = [.1, .8, .1]

#sensor model
ztxt = [.1, .1, .9, .1, .9, .1, .1, .1, .9, .1]

def prediction(prior, action):
	xp = [0]*len(prior)
	if action == 'right':
		for i in range(len(prior)):
			# 5 possible cases (gross)
			#stayed on cell (1)
			xp[i] = xtut[0] * prior[i]

			#moved one right (2)
			if(i-1 >= 0):
				xp[i] += xtut[1] * prior[i-1]

			#moved two right (3)
			if(i-2 >= 0):
				xp[i] += xtut[2] * prior[i-2]

			
	if action == 'left':
		for i in range(len(prior)):
			# The other 2 cases
			#stayed on cell (1) (again)
			xp[i] = xtut[0] * prior[i]

			#moved one left (4)
			if(i+1 < len(prior)):
				xp[i] += xtut[1] * prior[i+1]

			#moved two left (5)
			if(i+2 < len(prior)):
				xp[i] += xtut[2] * prior[i+2]

			
	return xp

def correction(prior, observation):
	#@TODO include observation in here somehow
	xc = [0] * len(prior)
	for i in range(len(prior)):
		#if we see a door
		if observation == True:
			xc[i] = ztxt[i] * prior[i]
		# if we dont see a door
		elif observation == False:
			xc[i] = (1 - ztxt[i]) * prior[i]
		norm += xc[i]
	#normalization
	for i in range(len(prior)):
		xc[i]/= norm
	return xc

def move(direction):
	numsteps = 0
	rng = rand.random()
	# first, determine the number of moves we actually move
	if rng > xtut[0] + xtut[1]:
		numsteps = 2
	elif rng > xtut[0]:
		numsteps = 1
	else:
		numsteps = 0
		

	# second, assign direction
	if direction == 'left':
		numsteps *= -1
	if direction == 'right':
		pass
	else:
		print("You typed left or right wrong")
	
	# last, 'clamp' the start and end indices
	real_position += numsteps;
	if real_position < 0:
		real_position = 0
	if real_position > 9:
		real_position = 9

	return real_position

# return if we see the door or not
def read(real_position):
	r = random.random()
	if r < ztxt[real_position]:
		return True
	else:
		return False

def run(direction):
	global x, real_position
	x = prediction(x, direction)	
	real_position = move(direction)
	
	observation = read(real_position)
	x = correction(pred, obs)
	return x

def get_max_index(arr):
	max_elt = 0;
	max_index = 0;
	for i in range(len(arr)):
		elt = arr[i]		
		if elt > max_elt:
			max_elt = elt
			max_index = i
	return max_index

	
for i in range(20):	
	for j in range(10):
		belief = run('right')
	for k in range(10):
		belief = run('left')
	#compute the maximum on our array of guesses
	guess = get_max_index(belief)
	print("real is", real_position, "guess is", guess)

