import numpy as npy 

steve = open('jobs_speech.txt').read()
jobs = steve.split()

#now find all the pairs 
def pair_generation(jobs):
	for x in range(len(jobs)-1):
		# generate the pairs
		yield(jobs[x], jobs[x+1])

pairings = pair_generation(jobs)

dict = {}
for x, y in pairings:
	if x in dict.keys():
		dict[x].append(y)
	else:
		dict[x] = y

start = npy.random.choice(jobs)

#create chain 
markov_chain = [start]
chain_length = 20

for i in range(chain_length):
	markov_chain.append(npy.random.choice(dict[markov_chain[-1]]))

''.join(markov_chain)



