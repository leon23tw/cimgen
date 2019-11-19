from cimpy.cimgen_v2_4_15_flat_9.Base import Base


class Inductance(Base):
	'''
	Inductive part of reactance (imaginary part of impedance), at rated frequency.

	:value:  Default: 0.0
	:unit:  Default: None
	:multiplier:  Default: None
		'''

	possibleProfileList = {'class': ['EQ', ],
						'value': ['EQ', ],
						'unit': ['EQ', ],
						'multiplier': ['EQ', ],
												}

	

	def __init__(self, value = 0.0, unit = None, multiplier = None,  ):
	
		self.value = value
		self.unit = unit
		self.multiplier = multiplier
		
	def __str__(self):
		str = 'class=Inductance\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
