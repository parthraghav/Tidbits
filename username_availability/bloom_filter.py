import math
import fnv
from bitarray import bitarray

class BloomFilter:
	def __init__(self, item_count : int, fp_prob : float):
		"""
		Args:
			item_count (int): Number of items contained in the bloom filter
			fp_prob (float): False Positive probability permitted
		"""
		self.fp_prob = fp_prob
		
		self.size = self.get_size(item_count, fp_prob)

		self.hash_count = self.get_hash_count(self.size, item_count)

		# initialize the bit array
		self.bit_array = bitarray(self.size)
		self.bit_array.setall(0)

		# initialise item digests (hashes created by hash functions)
		self.digests = [None] * self.hash_count

	def add(self, item : str) -> None:
		"""Adds an item to the boom filter
		"""		
		for i in range(self.hash_count):
			digest = self.get_digests(item)[i]
			self.bit_array[digest] = 1

	def check(self, item : str) -> bool:
		"""Verifies if an item is contained
		"""
		for i in range(self.hash_count):
			digest = self.get_digests(item)[i]
			if not self.bit_array[digest]:
				return False
		return True
	
	def get_digests(self, item : str) -> list:
		"""Generates digests for a string. Used in insertion and lookup.
		Inspired from http://willwhim.wpengine.com/2011/09/03/producing-n-hash-functions-by-hashing-only-once/
		"""		
		a = fnv.hash(str.encode(item), algorithm=fnv.fnv_1a)
		b = fnv.hash(str.encode(item), algorithm=fnv.fnv_1a)
		x = a % self.size
		for i in range(self.hash_count):
			self.digests[i] = (x + self.size) if x < 0 else x
			x = (x + b) % self.size
		return [int(digest) for digest in self.digests]

	def get_size(self, item_count : int, fp_prob : float) -> int:
		"""Compute the bit array size from item count and false positive probability.
		Formula borrowed from https://brilliant.org/wiki/bloom-filter/
		"""		
		return int(-1 * item_count * math.log(fp_prob) / (math.log(2) ** 2))
	
	def get_hash_count(self, bit_array_size: int, item_count: int) -> int:
		"""Compute the optimal number of hash functions needed for the bloom filter
		Formula borrowed from https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
		"""		
		return int(bit_array_size / item_count * math.log(2))