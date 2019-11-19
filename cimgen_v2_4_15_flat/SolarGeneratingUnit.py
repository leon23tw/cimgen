from cimpy.cimgen_v2_4_15_flat_9.GeneratingUnit import GeneratingUnit


class SolarGeneratingUnit(GeneratingUnit):
	'''
	A solar thermal generating unit.

		'''

	possibleProfileList = {'class': ['EQ', 'SSH', ],
												}

	__doc__ += '\n Documentation of parent class GeneratingUnit: \n' + GeneratingUnit.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=SolarGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
