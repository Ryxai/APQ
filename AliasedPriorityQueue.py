from collections import namedtuple, deque
class AliasedPriorityQueue:
	"""A priority queue that uses a sorting function to provide the ability to use
	custom priority identifiers. Queues can be accessed by identifier or by index
	(the standard method of accessing priority queues)
	"""
	
	AliasedQueue = namedtuple("AliasedQueue", "alias queue")
	def __init__(self, items = {}, sorting_func = lambda x: x):
		"""Initializes the AliasedPriorityQueue with labels and a priority function
		used to order the priority queue.
		:items: A list of tupled keys and values which are used as initial seed values
		for the aliases and the queue contents respectively
		:sorting_func: A key function used to transform the aliases into values so
		 the list of queues can be properly sorted"""
		if not hasattr(items, "__next__") or not hasattr(items, "__iter__"):
			raise TypeError("items must be an iterable")
		if not 
		used_aliases = set()
		self._queues = []
		for k, v in items:
			if k not in used_aliases:
				used_aliases.update(k)
				self._queues.append(AliasedQueue(alias = k, queue = deque(v)))
			else:
				if not hasattr(v, "__next__") or not hasattr(v, "__iter__"):
					self._queues[k].queue.append(v)
				else:
					#Flatten list
					for item in v:
						self._queues[k].queue.append(item)
		else:
			self._queues = sorted(self._queues, key = sorting_func)
		self._key_func = sorting_func
	
	def __dict__(self):
		"""Return a dictionary version of the AliasedPriorityQueue"""
		return {q.alias : list(q.queue) for q in self._queues}
	
	def __repr__(self):
		"""Returns a string representation of the AliasedPriorityQueue. However it is
		unable to print the key function as that item is dynamically defined at the 
		point of initialization."""
		return "AliasedPriorityQueue({0})".format(repr(dict(self)))

	def __str__(self):
		"""Returns a string representation of the AliasedPriorityQueue."""
		return "[{0}]".format(repr(dict(self)))
	
	def __hash__(self):
		"""Overrides the built in hash function"""
		bucket_max = 105000 
		hash_val = 0
		for k,v in self.dict().items():
			hash_val += hash(k) * sum([hash(item) for item in v])
		return (hash_val * hash(self._key_func)) % bucket_max
	
	def __eq__(self, other):
		"""Returns whether or not two AliasedPriorityQueue(s) are equal"""
		return hash(self) == hash(other)
	
	def __ne__(self, other):
		"""Returns whether or not two AliasedPriorityQueue(s) are not equal"""
		return hash(self) != hash(other)
	
	def enqueue(self, item, alias):
		"""Add an item to the aliased priority queue.
		
		:item: The item to be added to the 'alias' queue
		:alias: The alias of the given queue for the message to be added to"""
		self._get_queue_by_alias(alias).queue.append(item)
	
	
	def dequeue(self):
		"""Gets the next item from the highest priority queue where an item is 
		available. Used for iteration purposes"""
		for q in self._queues:
			if len(q) > 0:
				return q.popleft()
		else:
			raise StopIteration

	def add_queue(self, new_alias):
		"""Adds a new queue to the priority queue dynamically. Once the queue is
		added, the queues are sorted to be listed in the proper order based on the
		priority function. If the new queue is added the function returns true, 
		otherwise if the alias is already present in the queue list, the function returns
		false as the queue has already been added.false
		
		:new_alias: The alias of the new queue to be added
		:returns: A boolean representing whether the addition was successful or not"""
		if (alias in self.all_aliases()):
			return False
		else:
			self._queues.append(AliasedQueue(alias = new_alias, queue = deque()))
			self._queues = sorted(self._queues, key = sorting_func)
			return True
	
	def del_queue(self, alias):
		"""Attempts to delete an aliased queue with the provided alias. If the queue
		does not exist than the function returns false. If the queue exists than the 
		queue is deleted and the function returns true.
		
		:alias: The alias of the queue to be deleted
		:returns: A boolean representing whether the deletion was sucessful or not"""
		if (alias not in self.all_aliases()):
			return False
		else:	
			self._queues.remove(self._get_queue_by_alias(alias))
			return True
	
	def all_aliases(self):
		"""Returns all the aliases of the queues
		
		:returns: A list of all the aliases of all the queues"""
		return [queue.alias for queue in self._queues]
	
	def _get_queue_by_alias(self, alias):
		"""TODO: Get queue by alias docstring"""
		return [queue for queue in self._queues if queue.alias == alias]
