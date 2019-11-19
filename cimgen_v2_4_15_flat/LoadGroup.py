from cimpy.cimgen_v2_4_15_flat_9.IdentifiedObject import IdentifiedObject


class LoadGroup(IdentifiedObject):
	'''
	The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

		'''

	possibleProfileList = {'class': ['EQ', ],
												}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=LoadGroup\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
