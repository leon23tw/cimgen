from cimpy.cimgen_v2_4_15_flat_9.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAVR7(ExcitationSystemDynamics):
	'''
	IVO excitation system.

	:k1: Gain (K1).  Typical Value = 1. Default: 0.0
	:a1: Lead coefficient (A1).  Typical Value = 0.5. Default: 0.0
	:a2: Lag coefficient (A2).  Typical Value = 0.5. Default: 0.0
	:t1: Lead time constant (T1).  Typical Value = 0.05. Default: 0.0
	:t2: Lag time constant (T2).  Typical Value = 0.1. Default: 0.0
	:vmax1: Lead-lag max. limit (Vmax1).  Typical Value = 5. Default: 0.0
	:vmin1: Lead-lag min. limit (Vmin1).  Typical Value = -5. Default: 0.0
	:k3: Gain (K3).  Typical Value = 3. Default: 0.0
	:a3: Lead coefficient (A3).  Typical Value = 0.5. Default: 0.0
	:a4: Lag coefficient (A4).  Typical Value = 0.5. Default: 0.0
	:t3: Lead time constant (T3).  Typical Value = 0.1. Default: 0.0
	:t4: Lag time constant (T4).  Typical Value = 0.1. Default: 0.0
	:vmax3: Lead-lag max. limit (Vmax3).  Typical Value = 5. Default: 0.0
	:vmin3: Lead-lag min. limit (Vmin3).  Typical Value = -5. Default: 0.0
	:k5: Gain (K5).  Typical Value = 1. Default: 0.0
	:a5: Lead coefficient (A5).  Typical Value = 0.5. Default: 0.0
	:a6: Lag coefficient (A6).  Typical Value = 0.5. Default: 0.0
	:t5: Lead time constant (T5).  Typical Value = 0.1. Default: 0.0
	:t6: Lag time constant (T6).  Typical Value = 0.1. Default: 0.0
	:vmax5: Lead-lag max. limit (Vmax5).  Typical Value = 5. Default: 0.0
	:vmin5: Lead-lag min. limit (Vmin5).  Typical Value = -2. Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'k1': ['DY', ],
						'a1': ['DY', ],
						'a2': ['DY', ],
						't1': ['DY', ],
						't2': ['DY', ],
						'vmax1': ['DY', ],
						'vmin1': ['DY', ],
						'k3': ['DY', ],
						'a3': ['DY', ],
						'a4': ['DY', ],
						't3': ['DY', ],
						't4': ['DY', ],
						'vmax3': ['DY', ],
						'vmin3': ['DY', ],
						'k5': ['DY', ],
						'a5': ['DY', ],
						'a6': ['DY', ],
						't5': ['DY', ],
						't6': ['DY', ],
						'vmax5': ['DY', ],
						'vmin5': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, k1 = 0.0, a1 = 0.0, a2 = 0.0, t1 = 0.0, t2 = 0.0, vmax1 = 0.0, vmin1 = 0.0, k3 = 0.0, a3 = 0.0, a4 = 0.0, t3 = 0.0, t4 = 0.0, vmax3 = 0.0, vmin3 = 0.0, k5 = 0.0, a5 = 0.0, a6 = 0.0, t5 = 0.0, t6 = 0.0, vmax5 = 0.0, vmin5 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.k1 = k1
		self.a1 = a1
		self.a2 = a2
		self.t1 = t1
		self.t2 = t2
		self.vmax1 = vmax1
		self.vmin1 = vmin1
		self.k3 = k3
		self.a3 = a3
		self.a4 = a4
		self.t3 = t3
		self.t4 = t4
		self.vmax3 = vmax3
		self.vmin3 = vmin3
		self.k5 = k5
		self.a5 = a5
		self.a6 = a6
		self.t5 = t5
		self.t6 = t6
		self.vmax5 = vmax5
		self.vmin5 = vmin5
		
	def __str__(self):
		str = 'class=ExcAVR7\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
