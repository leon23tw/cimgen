from cimpy.cimgen_v2_4_15_flat_9.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroWPID(TurbineGovernorDynamics):
	'''
	Woodward PID Hydro Governor.

	:mwbase: Base for power values  (MWbase) (>0).  Unit = MW. Default: 0.0
	:treg: Speed detector time constant (Treg). Default: 0.0
	:reg: Permanent drop (Reg). Default: 0.0
	:kp: Proportional gain (Kp).  Typical Value = 0.1. Default: 0.0
	:ki: Reset gain (Ki).  Typical Value = 0.36. Default: 0.0
	:kd: Derivative gain (Kd).  Typical Value = 1.11. Default: 0.0
	:ta: Controller time constant (Ta) (>0).  Typical Value = 0. Default: 0.0
	:tb: Gate servo time constant (Tb) (>0).  Typical Value = 0. Default: 0.0
	:velmax: Maximum gate opening velocity (Velmax).  Unit = PU/sec.  Typical Value = 0. Default: 0.0
	:velmin: Maximum gate closing velocity (Velmin).  Unit = PU/sec.  Typical Value = 0. Default: 0.0
	:gatmax: Gate opening Limit Maximum (Gatmax). Default: 0.0
	:gatmin: Gate opening Limit Minimum (Gatmin). Default: 0.0
	:tw: Water inertia time constant (Tw) (>0).  Typical Value = 0. Default: 0.0
	:pmax: Maximum Power Output (Pmax). Default: 0.0
	:pmin: Minimum Power Output (Pmin). Default: 0.0
	:d: Turbine damping factor (D).  Unit = delta P / delta speed. Default: 0.0
	:gv3: Gate position 3 (Gv3). Default: 0.0
	:gv1: Gate position 1 (Gv1). Default: 0.0
	:pgv1: Output at Gv1 PU of MWbase (Pgv1). Default: 0.0
	:gv2: Gate position 2 (Gv2). Default: 0.0
	:pgv2: Output at Gv2 PU of MWbase (Pgv2). Default: 0.0
	:pgv3: Output at Gv3 PU of MWbase (Pgv3). Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'mwbase': ['DY', ],
						'treg': ['DY', ],
						'reg': ['DY', ],
						'kp': ['DY', ],
						'ki': ['DY', ],
						'kd': ['DY', ],
						'ta': ['DY', ],
						'tb': ['DY', ],
						'velmax': ['DY', ],
						'velmin': ['DY', ],
						'gatmax': ['DY', ],
						'gatmin': ['DY', ],
						'tw': ['DY', ],
						'pmax': ['DY', ],
						'pmin': ['DY', ],
						'd': ['DY', ],
						'gv3': ['DY', ],
						'gv1': ['DY', ],
						'pgv1': ['DY', ],
						'gv2': ['DY', ],
						'pgv2': ['DY', ],
						'pgv3': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, treg = 0.0, reg = 0.0, kp = 0.0, ki = 0.0, kd = 0.0, ta = 0.0, tb = 0.0, velmax = 0.0, velmin = 0.0, gatmax = 0.0, gatmin = 0.0, tw = 0.0, pmax = 0.0, pmin = 0.0, d = 0.0, gv3 = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, pgv3 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.treg = treg
		self.reg = reg
		self.kp = kp
		self.ki = ki
		self.kd = kd
		self.ta = ta
		self.tb = tb
		self.velmax = velmax
		self.velmin = velmin
		self.gatmax = gatmax
		self.gatmin = gatmin
		self.tw = tw
		self.pmax = pmax
		self.pmin = pmin
		self.d = d
		self.gv3 = gv3
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.pgv3 = pgv3
		
	def __str__(self):
		str = 'class=GovHydroWPID\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
