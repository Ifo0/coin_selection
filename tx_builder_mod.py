#!/usr/bin/python3
import random



def get_inputs(utxo_set, amount, fee):
	"""
 	this function should return a subset of utxo_set
 	such that total amount in the list is
 	more than (amount + fee) and change is minimal
	"""

	"""
	Ivo's logic:
	This file is a small modification to the original you sent me.
	I wanted to find the *best* subset of inputs to create a transaction with.
	The best subset is the one that would generate the smallest change.
	This is achived by generating a population of input subsets, where each subset
	contains randomly selected utxo's.
	I assume that a large enough population, would contain an optimum or a nearly optimum
	solution on most cases.
	"""


	inputs = []
	dict = {}
	total = 0
	#Magic range;
	#Assumption: within 20 iterations a subest would definately be found
	#that satisfy the condition total >= amount + fee
	for num in range(1,21):
		selection = random.choice(utxo_set)
		total += selection[2]
		 # add amount to total
		inputs.append(selection)
		# append to the list
		# if we get enough amount in the inputs
		if total >= amount + fee:
			return inputs

	return inputs


if __name__ == '__main__':

	# available inputs for spending
	# have a form (prev_txid, prev_output, amount)
	utxo_set = [
		("7078d48ca924c92643dac992756a08bf340e096fe49680c280b37cbe3e3c6761", 0, 4786),
		("78a30be97918f2895825904585c04db79881ded24f8629c0c728e805e8577aa7", 1, 436287),
		("50366207409620e23288b2961ea7572dc620ad01721ea36a057083c9924525a4", 0, 2892),
		("1239f31407a323a40ac3c7695467d22eb1b80251cef10f28cbea704bc362a90a", 2, 854739),
		("3bd096d7d422da18b3970dbe1a701b02384a36deed3c90696408ff3b11a3d685", 1, 19382),
		("1b4abd626bdbab1eb119cd740fda10b9abb3f3b90a991a9579fcd144c16f73cc", 5, 423154),
		("e98c10c4b888fbdb9e285dac6782a373456cc88a9eb7aa73c16aa261253bae20", 1, 49382691),
	]

	amount = 470000 # amount to send
	fee = 1500 # fee
	amountAndFee = amount + fee

	data_structure = {}

	#Get inputs return a list of randomly selected inputs.
	#The function is run 199 (magic) times, each time reutrning a list of inputs
	#that is stored in a dictionary. The key of the dictionary is the total value
	#of the inputs
	#After the iternations are complete, we check the list of keys to find the
	#key with the smallest value. This key would correspond to a subset of
	#inputs that generate the least change.
	#This subset is stored in the best_selection variable and used for the transaction
	#I am aware that the keys may be overwritten if another subsets amouts to The
	#same total value, but let's ignore that for now.
	for num in range(1, 200):
		inputs = get_inputs(utxo_set, amount, fee)
		total = 0
		for tuple in inputs:
			total += tuple[2]
		data_structure[total] = inputs
	print(data_structure.keys())
	print("Number of unique subsets generated:", len(data_structure))
	print("\n")
	min_diff = min(data_structure.keys())
	best_selection = data_structure[min_diff]
	





	# result:
	print("Requested sum: ", amount)
	print("Requested fee:", fee)
	print("UTXO subset:")
	print(best_selection)
	print("Length of the subset is:", len(best_selection))
	total = sum([txin[2] for txin in best_selection])
	print("In total:", total)
	print("Change:", total-amount-fee)
