from cimpy.cimgen_v2_4_15_flat_9.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss5(PowerSystemStabilizerDynamics):
	'''
	Italian PSS - Detailed PSS.

	:kpe: Electric power input gain (K).  Typical Value = 0.3. Default: 0.0
	:kf: Frequency/shaft speed input gain (K).  Typical Value = 5. Default: 0.0
	:isfreq: Selector for Frequency/shaft speed input (IsFreq). true = speed false = frequency. Typical Value = true. Default: False
	:kpss: PSS gain (K).  Typical Value = 1. Default: 0.0
	:ctw2: Selector for Second washout enabling (C). true = second washout filter is bypassed false = second washout filter in use. Typical Value = true. Default: False
	:tw1: First WashOut (T).  Typical Value = 3.5. Default: 0.0
	:tw2: Second WashOut (T).  Typical Value = 0. Default: 0.0
	:tl1: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
	:tl2: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
	:tl3: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
	:tl4: Lead/lag time constant (T).  Typical Value = 0. Default: 0.0
	:vsmn: Stabilizer output max limit (V).  Typical Value = -0.1. Default: 0.0
	:vsmx: Stabilizer output min limit (V).  Typical Value = 0.1. Default: 0.0
	:tpe: Electric power filter time constant (T).  Typical Value = 0.05. Default: 0.0
	:pmm: Minimum power PSS enabling (P).  Typical Value = 0.25. Default: 0.0
	:deadband: Stabilizer output dead band (DeadBand).  Typical Value = 0. Default: 0.0
	:vadat:  Default: False
		'''

	possibleProfileList = {'class': ['DY', ],
						'kpe': ['DY', ],
						'kf': ['DY', ],
						'isfreq': ['DY', ],
						'kpss': ['DY', ],
						'ctw2': ['DY', ],
						'tw1': ['DY', ],
						'tw2': ['DY', ],
						'tl1': ['DY', ],
						'tl2': ['DY', ],
						'tl3': ['DY', ],
						'tl4': ['DY', ],
						'vsmn': ['DY', ],
						'vsmx': ['DY', ],
						'tpe': ['DY', ],
						'pmm': ['DY', ],
						'deadband': ['DY', ],
						'vadat': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, kpe = 0.0, kf = 0.0, isfreq = False, kpss = 0.0, ctw2 = False, tw1 = 0.0, tw2 = 0.0, tl1 = 0.0, tl2 = 0.0, tl3 = 0.0, tl4 = 0.0, vsmn = 0.0, vsmx = 0.0, tpe = 0.0, pmm = 0.0, deadband = 0.0, vadat = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kpe = kpe
		self.kf = kf
		self.isfreq = isfreq
		self.kpss = kpss
		self.ctw2 = ctw2
		self.tw1 = tw1
		self.tw2 = tw2
		self.tl1 = tl1
		self.tl2 = tl2
		self.tl3 = tl3
		self.tl4 = tl4
		self.vsmn = vsmn
		self.vsmx = vsmx
		self.tpe = tpe
		self.pmm = pmm
		self.deadband = deadband
		self.vadat = vadat
		
	def __str__(self):
		str = 'class=Pss5\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
