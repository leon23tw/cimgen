from cimpy.cimgen_v2_4_15_flat_9.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovHydroIEEE2(TurbineGovernorDynamics):
	'''
	IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-dashpot governors.  Ref

	:mwbase: Base for power values (MWbase) (> 0).  Unit = MW. Default: 0.0
	:tg: Gate servo time constant (Tg).  Typical Value = 0.5. Default: 0.0
	:tp: Pilot servo valve time constant (Tp).  Typical Value = 0.03. Default: 0.0
	:uo: Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1. Default: 0.0
	:uc: Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1. Default: 0.0
	:pmax: Maximum gate opening (Pmax).  Typical Value = 1. Default: 0.0
	:pmin: Minimum gate opening (Pmin).  Typical Value = 0. Default: 0.0
	:rperm: Permanent droop (Rperm).  Typical Value = 0.05. Default: 0.0
	:rtemp: Temporary droop (Rtemp).  Typical Value = 0.5. Default: 0.0
	:tr: Dashpot time constant (Tr).  Typical Value = 12. Default: 0.0
	:tw: Water inertia time constant (Tw).  Typical Value = 2. Default: 0.0
	:kturb: Turbine gain (Kturb).  Typical Value = 1. Default: 0.0
	:aturb: Turbine numerator multiplier (Aturb).  Typical Value = -1. Default: 0.0
	:bturb: Turbine denominator multiplier (Bturb).  Typical Value = 0.5. Default: 0.0
	:gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0. Default: 0.0
	:pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0. Default: 0.0
	:gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0. Default: 0.0
	:pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0. Default: 0.0
	:gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0. Default: 0.0
	:pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0. Default: 0.0
	:gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0. Default: 0.0
	:pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0. Default: 0.0
	:gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0. Default: 0.0
	:pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0. Default: 0.0
	:gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0. Default: 0.0
	:pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0. Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'mwbase': ['DY', ],
						'tg': ['DY', ],
						'tp': ['DY', ],
						'uo': ['DY', ],
						'uc': ['DY', ],
						'pmax': ['DY', ],
						'pmin': ['DY', ],
						'rperm': ['DY', ],
						'rtemp': ['DY', ],
						'tr': ['DY', ],
						'tw': ['DY', ],
						'kturb': ['DY', ],
						'aturb': ['DY', ],
						'bturb': ['DY', ],
						'gv1': ['DY', ],
						'pgv1': ['DY', ],
						'gv2': ['DY', ],
						'pgv2': ['DY', ],
						'gv3': ['DY', ],
						'pgv3': ['DY', ],
						'gv4': ['DY', ],
						'pgv4': ['DY', ],
						'gv5': ['DY', ],
						'pgv5': ['DY', ],
						'gv6': ['DY', ],
						'pgv6': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, tg = 0.0, tp = 0.0, uo = 0.0, uc = 0.0, pmax = 0.0, pmin = 0.0, rperm = 0.0, rtemp = 0.0, tr = 0.0, tw = 0.0, kturb = 0.0, aturb = 0.0, bturb = 0.0, gv1 = 0.0, pgv1 = 0.0, gv2 = 0.0, pgv2 = 0.0, gv3 = 0.0, pgv3 = 0.0, gv4 = 0.0, pgv4 = 0.0, gv5 = 0.0, pgv5 = 0.0, gv6 = 0.0, pgv6 = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.tg = tg
		self.tp = tp
		self.uo = uo
		self.uc = uc
		self.pmax = pmax
		self.pmin = pmin
		self.rperm = rperm
		self.rtemp = rtemp
		self.tr = tr
		self.tw = tw
		self.kturb = kturb
		self.aturb = aturb
		self.bturb = bturb
		self.gv1 = gv1
		self.pgv1 = pgv1
		self.gv2 = gv2
		self.pgv2 = pgv2
		self.gv3 = gv3
		self.pgv3 = pgv3
		self.gv4 = gv4
		self.pgv4 = pgv4
		self.gv5 = gv5
		self.pgv5 = pgv5
		self.gv6 = gv6
		self.pgv6 = pgv6
		
	def __str__(self):
		str = 'class=GovHydroIEEE2\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
