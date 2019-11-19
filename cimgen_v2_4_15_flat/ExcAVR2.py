from cimpy.cimgen_v2_4_15_flat_9.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR2(ExcitationSystemDynamics):
	'''
	Italian excitation system corresponding to IEEE (1968) Type 2 Model. It represents alternator and rotating diodes and electromechanic voltage regulators.

	:ka: AVR gain (K).  Typical Value = 500. Default: 0.0
	:vrmn: Maximum AVR output (V).  Typical Value = -6. Default: 0.0
	:vrmx: Minimum AVR output (V).  Typical Value = 7. Default: 0.0
	:ta: AVR time constant (T).  Typical Value = 0.02. Default: 0.0
	:tb: AVR time constant (T).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant (T).  Typical Value = 1. Default: 0.0
	:e1: Field voltage value 1 (E1).  Typical Value = 4.18. Default: 0.0
	:se1: Saturation factor at E1 (S(E1)).  Typical Value = 0.1. Default: 0.0
	:e2: Field voltage value 2 (E2).  Typical Value = 3.14. Default: 0.0
	:se2: Saturation factor at E2 (S(E2)).  Typical Value = 0.03. Default: 0.0
	:kf: Rate feedback gain (K).  Typical Value = 0.02. Default: 0.0
	:tf1: Rate feedback time constant (T).  Typical Value = 1. Default: 0.0
	:tf2: Rate feedback time constant (T).  Typical Value = 1. Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'ka': ['DY', ],
						'vrmn': ['DY', ],
						'vrmx': ['DY', ],
						'ta': ['DY', ],
						'tb': ['DY', ],
						'te': ['DY', ],
						'e1': ['DY', ],
						'se1': ['DY', ],
						'e2': ['DY', ],
						'se2': ['DY', ],
						'kf': ['DY', ],
						'tf1': ['DY', ],
						'tf2': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, vrmn = 0.0, vrmx = 0.0, ta = 0.0, tb = 0.0, te = 0.0, e1 = 0.0, se1 = 0.0, e2 = 0.0, se2 = 0.0, kf = 0.0, tf1 = 0.0, tf2 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.vrmn = vrmn
		self.vrmx = vrmx
		self.ta = ta
		self.tb = tb
		self.te = te
		self.e1 = e1
		self.se1 = se1
		self.e2 = e2
		self.se2 = se2
		self.kf = kf
		self.tf1 = tf1
		self.tf2 = tf2
		
	def __str__(self):
		str = 'class=ExcAVR2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
