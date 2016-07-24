ALLERGIES = [
				'eggs',
				'peanuts',
				'shellfish',
				'strawberries',
				'tomatoes',
				'chocolate',
				'pollen',
				'cats',
			]

class Allergies(object):
	def __init__(self, score):
		self.lst = [allergy for index, allergy in enumerate(ALLERGIES) if 1 << index & score]

	def is_allergic_to(self, item):
		return item in self.lst