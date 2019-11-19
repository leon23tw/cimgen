from cimpy.cimgen_v2_4_15_flat_9.TapChanger import TapChanger


class RatioTapChanger(TapChanger):
	'''
	A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.

	:tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Default: None
	:stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position. Default: 0.0
	:RatioTapChangerTable: The ratio tap changer of this tap ratio table. Default: None
	:TransformerEnd: Ratio tap changer associated with this transformer end. Default: None
		'''

	possibleProfileList = {'class': ['EQ', 'SSH', ],
						'tculControlMode': ['EQ', ],
						'stepVoltageIncrement': ['EQ', ],
						'RatioTapChangerTable': ['EQ', ],
						'TransformerEnd': ['EQ', ],
												}

	__doc__ += '\n Documentation of parent class TapChanger: \n' + TapChanger.__doc__ 

	def __init__(self, tculControlMode = None, stepVoltageIncrement = 0.0, RatioTapChangerTable = None, TransformerEnd = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.tculControlMode = tculControlMode
		self.stepVoltageIncrement = stepVoltageIncrement
		self.RatioTapChangerTable = RatioTapChangerTable
		self.TransformerEnd = TransformerEnd
		
	def __str__(self):
		str = 'class=RatioTapChanger\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
