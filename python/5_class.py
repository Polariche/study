"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
__init__(self) : called when an instance is created.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Bird:
	"""It's a bird! Chirp chirp!"""
	beak = "sharp"
	legs = "short"
	wings = "strong"
	wingspan = 9001

	def __init__(self,name: str):
		self.status = "newly hatched"   #It 'Springs into existence' when it isn't defined. Kinda like lua...
		self.name = name
		self.call_status()

	def chirp(self): 
		print('chirp chirp!')

	def feed(self):
		print(self.name + ' is enjoying its meal.')

	def call_status(self):
		print(self.name + ' is '+self.status)

Bird = Bird('chirpy')
Bird.chirp()
Bird.feed()