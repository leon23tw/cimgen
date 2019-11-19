from cimpy.cimgen_v2_4_15_flat_9.DCConductingEquipment import DCConductingEquipment


class DCChopper(DCConductingEquipment):
	'''
	Low resistance equipment used in the internal DC circuit to balance voltages. It has typically positive and negative pole terminals and a ground.

		'''

	possibleProfileList = {'class': ['EQ', ],
												}

	__doc__ += '\n Documentation of parent class DCConductingEquipment: \n' + DCConductingEquipment.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=DCChopper\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
