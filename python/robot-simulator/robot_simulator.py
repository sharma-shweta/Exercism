NORTH, EAST, SOUTH, WEST = range(4)

class Robot(object):
	def __init__(self, bearing=NORTH, x=0, y=0):
		self.x = x
		self.y = y
		self.bearing = bearing

	@property
	def coordinates(self):
		return (self.x, self.y)

	def turn_right(self):
		self.bearing = (self.bearing + 1)%4

	def turn_left(self):
		self.bearing = (self.bearing - 1)%4

	def advance(self):
		self.x += [0, 1, 0, -1][self.bearing]
		self.y += [1, 0, -1, 0][self.bearing]

	def simulate(self, path):
		instructions = {'L': self.turn_left, 'R': self.turn_right, 'A': self.advance}
		for instr in path:
			instructions[instr.upper()]()
