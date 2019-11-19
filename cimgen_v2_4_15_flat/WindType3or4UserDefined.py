from cimpy.cimgen_v2_4_15_flat_9.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics


class WindType3or4UserDefined(WindTurbineType3or4Dynamics):
	'''
	Wind Type 3 or Type 4 function block whose dynamic behaviour is described by

	:proprietary: Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. Default: False
	:ProprietaryParameterDynamics: Parameter of this proprietary user-defined model. Default: []
		'''

	possibleProfileList = {'class': ['DY', ],
						'proprietary': ['DY', ],
						'ProprietaryParameterDynamics': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class WindTurbineType3or4Dynamics: \n' + WindTurbineType3or4Dynamics.__doc__ 

	def __init__(self, proprietary = False, ProprietaryParameterDynamics = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.proprietary = proprietary
		self.ProprietaryParameterDynamics = ProprietaryParameterDynamics
		
	def __str__(self):
		str = 'class=WindType3or4UserDefined\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
