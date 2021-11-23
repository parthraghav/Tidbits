from typing import Optional
from bloom_filter import BloomFilter

class AvailabilityChecker:
	MAX_USERNAMES_ALLOWED_DEFAULT = 1e3
	def __init__(self):
		self.username_count = 0
		self._make()
	
	def _make(self, expansion_multiple : int = 1, false_positive_tolerance : float = 0.05):
		self.max_usernames_allowed = self.MAX_USERNAMES_ALLOWED_DEFAULT * expansion_multiple
		self.false_positive_tolerance = false_positive_tolerance
		self.bloom_filter = BloomFilter(int(self.max_usernames_allowed), self.false_positive_tolerance)
	
	def _rebuild(self, expansion_multiple : int, data : Optional[list]):
		self._make(expansion_multiple)
		for entry in data:
			self.add(entry, should_bypass_availability_verification= True)

	def add_username(self, username: str, should_bypass_availability_verification: Optional[bool] = False) -> None:
		# Rebuild the filter with a greater size each time
		if self.username_count >= self.max_usernames_allowed:
			self._rebuild(expansion_multiple = 1e4)
		
		# Verify that the username is available
		if not should_bypass_availability_verification:
			assert(not self.is_username_taken(username))

		self.bloom_filter.add(username)
		self.username_count += 1

	def is_username_taken(self, username: str) -> bool:
		return self.bloom_filter.check(username)