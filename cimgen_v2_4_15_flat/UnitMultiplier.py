from cimpy.cimgen_v2_4_15_flat_9.Base import Base


class UnitMultiplier(Base):
	'''
	The unit multipliers defined for the CIM.

		'''

	possibleProfileList = {'class': ['DI', 'DY', 'EQ', 'SV', 'SSH', ],
												}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=UnitMultiplier\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
