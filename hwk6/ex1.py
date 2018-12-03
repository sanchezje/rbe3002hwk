from __future__ import print_function
import random as rand

#global variables because I'm lazy
real_position = 0 # assert the starting pos is always 0


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

			pass
	if action == 'left':
		for i in range(len(prior)):
			# 5 possible cases (gross)
			#stayed on cell (1)
			xp[i] = xtut[0] * prior[i]

			#moved one left (2)
			if(i+1 < len(prior)):
				xp[i] += xtut[1] * prior[i+1]

			#moved two left (3)
			if(i+2 < len(prior)):
				xp[i] += xtut[2] * prior[i+2]

			pass
	return xp
	
def correction(prior, observation):
	#@TODO include observation in here somehow
	xc = [0] * len(prior)
	for i in range(len(prior)):
		xc[i] = ztxt[i] * prior[i]
		norm += xc[i]
	#normalization
	for i in range(len(prior)):
		xc[i]/= norm
	return xc

def move(direction):
	numsteps = 0
	rng = rand.random()
	# first, determine the number of moves we actually move
	if rand > .9:
		numsteps = 2
	elif rand > .1:
		numsteps = 1
	else
		numsteps = 0
		

	# second, assign direction
	if direction == 'left':
		numsteps *= -1
	if direction == 'right':
		pass
	else
		print("You typed left or right wrong")
	
	# last, 'clamp' the start and end indices
	real_position += numsteps;
	if real_position < 0:
		real_position = 0
	if real_position > 9:
		real_position = 9

	return real_position
	
def read(real_position):
	pass

def run():
	# for every move
	# @TODO move the robot
	# @TODO get a new reading
	# @TODO update belief
		# first, move
		move('right')
		# next compute our prediction
		xp = prediction(x, 'right')

		# next, retrieve an observaton given our real position in space
		z = read(real_position)
		
		# next, compute our correction
		xc = correction(x, z)


if __name_ == "__main__:"
	run()
