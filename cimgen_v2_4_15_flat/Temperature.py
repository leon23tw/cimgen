from cimpy.cimgen_v2_4_15_flat_9.Base import Base


class Temperature(Base):
	'''
	Value of temperature in degrees Celsius.

	:multiplier:  Default: None
	:unit:  Default: None
	:value:  Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', 'EQ', ],
						'multiplier': ['DY', 'EQ', ],
						'unit': ['DY', 'EQ', ],
						'value': ['DY', 'EQ', ],
												}

	

	def __init__(self, multiplier = None, unit = None, value = 0.0,  ):
	
		self.multiplier = multiplier
		self.unit = unit
		self.value = value
		
	def __str__(self):
		str = 'class=Temperature\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
