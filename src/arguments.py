import argparse
import latency

def arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", type=str)
	parser.add_argument("-a", type=int)
	parser.add_argument("-b", type=int)
	args = parser.parse_args()

	target = args.t
	portMin = args.a
	portMax = args.b

	latency.latency(portMin, portMax, target);