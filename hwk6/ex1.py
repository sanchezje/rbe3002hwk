from __future__ import print_function

#prior
x = [.1] * 10

#actuation model
xtut = [.1, .8, .1]

#sensor model
ztxt = [.1, .1, .9, .1, .9, .1, .1, .1, .9, .1]

def prediction(prior, action):
	xp = [0]*len(prior)
	for i in range(len(prior)):
		#...

	return xp

def correction(prior, observation):
	xc = [0] * len(prior)
	for i in range(len(prior)):
		#...
	return xc

def run():
	# for every move
	# @TODO move the robot
	# @TODO get a new reading
	# @TODO update belief

if __name_ == "__main__:"
	run()
