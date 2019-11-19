from cimpy.cimgen_v2_4_15_flat_9.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovGAST3(TurbineGovernorDynamics):
	'''
	Generic turbogas with acceleration and temperature controller.

	:bp: Droop (bp).  Typical Value = 0.05. Default: 0.0
	:tg: Time constant of speed governor (Tg).  Typical Value = 0.05. Default: 0.0
	:rcmx: Maximum fuel flow (RCMX).  Typical Value = 1. Default: 0.0
	:rcmn: Minimum fuel flow (RCMN).  Typical Value = -0.1. Default: 0.0
	:ky: Coefficient of transfer function of fuel valve positioner (Ky).  Typical Value = 1. Default: 0.0
	:ty: Time constant of fuel valve positioner (Ty).  Typical Value = 0.2. Default: 0.0
	:tac: Fuel control time constant (Tac).  Typical Value = 0.1. Default: 0.0
	:kac: Fuel system feedback (K).  Typical Value = 0. Default: 0.0
	:tc: Compressor discharge volume time constant (Tc).  Typical Value = 0.2. Default: 0.0
	:bca: Acceleration limit set-point (Bca).  Unit = 1/s.  Typical Value = 0.01. Default: 0.0
	:kca: Acceleration control integral gain (Kca). Unit = 1/s.  Typical Value = 100. Default: 0.0
	:dtc: Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (deltaTc).  Typical Value = 390. Default: 0.0
	:ka: Minimum fuel flow (Ka).  Typical Value = 0.23. Default: 0.0
	:tsi: Time constant of radiation shield (Tsi).  Typical Value = 15. Default: 0.0
	:ksi: Gain of radiation shield (Ksi).  Typical Value = 0.8. Default: 0.0
	:ttc: Time constant of thermocouple (Ttc).  Typical Value = 2.5. Default: 0.0
	:tfen: Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical Value = 540. Default: 0.0
	:td: Temperature controller derivative gain (Td).  Typical Value = 3.3. Default: 0.0
	:tt: Temperature controller integration rate (Tt).  Typical Value = 250. Default: 0.0
	:mxef: Fuel flow maximum positive error value (MX).  Typical Value = 0.05. Default: 0.0
	:mnef: Fuel flow maximum negative error value (MN).  Typical Value = -0.05. Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'bp': ['DY', ],
						'tg': ['DY', ],
						'rcmx': ['DY', ],
						'rcmn': ['DY', ],
						'ky': ['DY', ],
						'ty': ['DY', ],
						'tac': ['DY', ],
						'kac': ['DY', ],
						'tc': ['DY', ],
						'bca': ['DY', ],
						'kca': ['DY', ],
						'dtc': ['DY', ],
						'ka': ['DY', ],
						'tsi': ['DY', ],
						'ksi': ['DY', ],
						'ttc': ['DY', ],
						'tfen': ['DY', ],
						'td': ['DY', ],
						'tt': ['DY', ],
						'mxef': ['DY', ],
						'mnef': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, bp = 0.0, tg = 0.0, rcmx = 0.0, rcmn = 0.0, ky = 0.0, ty = 0.0, tac = 0.0, kac = 0.0, tc = 0.0, bca = 0.0, kca = 0.0, dtc = 0.0, ka = 0.0, tsi = 0.0, ksi = 0.0, ttc = 0.0, tfen = 0.0, td = 0.0, tt = 0.0, mxef = 0.0, mnef = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.bp = bp
		self.tg = tg
		self.rcmx = rcmx
		self.rcmn = rcmn
		self.ky = ky
		self.ty = ty
		self.tac = tac
		self.kac = kac
		self.tc = tc
		self.bca = bca
		self.kca = kca
		self.dtc = dtc
		self.ka = ka
		self.tsi = tsi
		self.ksi = ksi
		self.ttc = ttc
		self.tfen = tfen
		self.td = td
		self.tt = tt
		self.mxef = mxef
		self.mnef = mnef
		
	def __str__(self):
		str = 'class=GovGAST3\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
