from cimpy.cimgen_v2_4_15_flat_9.RotatingMachineDynamics import RotatingMachineDynamics


class SynchronousMachineDynamics(RotatingMachineDynamics):
	'''
	Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following forms:

	:SynchronousMachine: Synchronous machine to which synchronous machine dynamics model applies. Default: None
	:TurbineGovernorDynamics: Synchronous machine model with which this turbine-governor model is associated. Default: []
	:ExcitationSystemDynamics: Excitation system model associated with this synchronous machine model. Default: None
	:MechanicalLoadDynamics: Mechanical load model associated with this synchronous machine model. Default: None
	:GenICompensationForGenJ: Compensation of voltage compensator's generator for current flow out of this  generator. Default: []
		'''

	possibleProfileList = {'class': ['DY', ],
						'SynchronousMachine': ['DY', ],
						'TurbineGovernorDynamics': ['DY', ],
						'ExcitationSystemDynamics': ['DY', ],
						'MechanicalLoadDynamics': ['DY', ],
						'GenICompensationForGenJ': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class RotatingMachineDynamics: \n' + RotatingMachineDynamics.__doc__ 

	def __init__(self, SynchronousMachine = None, TurbineGovernorDynamics = [], ExcitationSystemDynamics = None, MechanicalLoadDynamics = None, GenICompensationForGenJ = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.SynchronousMachine = SynchronousMachine
		self.TurbineGovernorDynamics = TurbineGovernorDynamics
		self.ExcitationSystemDynamics = ExcitationSystemDynamics
		self.MechanicalLoadDynamics = MechanicalLoadDynamics
		self.GenICompensationForGenJ = GenICompensationForGenJ
		
	def __str__(self):
		str = 'class=SynchronousMachineDynamics\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
