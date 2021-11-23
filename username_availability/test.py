import unittest
from availability_checker import AvailabilityChecker
import string
import random

def generate_rand_string(size=6, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(size))

class AvailabilityCheckerTest(unittest.TestCase):
	def test(self):
		with self.assertRaises(AssertionError) as context:
			checker = AvailabilityChecker()
			usernames = [ generate_rand_string() for _ in range(int(1e3))]
			for username in usernames:
				checker.add_username(username)
			for username in usernames:
				checker.add_username(username)

if __name__ == '__main__':
    unittest.main()
