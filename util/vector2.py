class Vector2():
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "<{},{}>".format(self.x, self.y)

	def __eq__(self, o: object) -> bool:
		return isinstance(o, Vector2) and o.x == self.x and o.y == self.y

	def invert(self):
		# TODO: make sure the math here is sound
		return Vector2(self.x * -1, self.y * -1)

	def __add__(self, other):
		return Vector2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector2(self.x - other.x, self.y - other.y)


UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)