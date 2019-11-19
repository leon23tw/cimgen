from cimpy.cimgen_v2_4_15_flat_9.TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteamEU(TurbineGovernorDynamics):
	'''
	Simplified model  of boiler and steam turbine with PID governor.

	:mwbase: Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
	:tp: Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0.0
	:ke: Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0
	:tip: Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0.0
	:tdp: Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0.0
	:tfp: Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0.0
	:tf: Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0.0
	:kfcor: Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0
	:db1: Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0
	:wfmax: Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0
	:wfmin: Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0
	:pmax: Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0
	:ten: Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0.0
	:tw: Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0.0
	:kwcor: Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0
	:db2: Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0
	:wwmax: Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0
	:wwmin: Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0
	:wmax1: Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0
	:wmax2: Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0
	:tvhp: Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0.0
	:cho: Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0
	:chc: Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0
	:hhpmax: Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0
	:tvip: Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0.0
	:cio: Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0
	:cic: Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0
	:simx: Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0
	:thp: High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0.0
	:trh: Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0.0
	:tlp: Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0.0
	:prhmax: Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0
	:khp: Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0
	:klp: Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0
	:tb: Boiler time constant (Tb).  Typical Value = 100. Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'mwbase': ['DY', ],
						'tp': ['DY', ],
						'ke': ['DY', ],
						'tip': ['DY', ],
						'tdp': ['DY', ],
						'tfp': ['DY', ],
						'tf': ['DY', ],
						'kfcor': ['DY', ],
						'db1': ['DY', ],
						'wfmax': ['DY', ],
						'wfmin': ['DY', ],
						'pmax': ['DY', ],
						'ten': ['DY', ],
						'tw': ['DY', ],
						'kwcor': ['DY', ],
						'db2': ['DY', ],
						'wwmax': ['DY', ],
						'wwmin': ['DY', ],
						'wmax1': ['DY', ],
						'wmax2': ['DY', ],
						'tvhp': ['DY', ],
						'cho': ['DY', ],
						'chc': ['DY', ],
						'hhpmax': ['DY', ],
						'tvip': ['DY', ],
						'cio': ['DY', ],
						'cic': ['DY', ],
						'simx': ['DY', ],
						'thp': ['DY', ],
						'trh': ['DY', ],
						'tlp': ['DY', ],
						'prhmax': ['DY', ],
						'khp': ['DY', ],
						'klp': ['DY', ],
						'tb': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class TurbineGovernorDynamics: \n' + TurbineGovernorDynamics.__doc__ 

	def __init__(self, mwbase = 0.0, tp = 0.0, ke = 0.0, tip = 0.0, tdp = 0.0, tfp = 0.0, tf = 0.0, kfcor = 0.0, db1 = 0.0, wfmax = 0.0, wfmin = 0.0, pmax = 0.0, ten = 0.0, tw = 0.0, kwcor = 0.0, db2 = 0.0, wwmax = 0.0, wwmin = 0.0, wmax1 = 0.0, wmax2 = 0.0, tvhp = 0.0, cho = 0.0, chc = 0.0, hhpmax = 0.0, tvip = 0.0, cio = 0.0, cic = 0.0, simx = 0.0, thp = 0.0, trh = 0.0, tlp = 0.0, prhmax = 0.0, khp = 0.0, klp = 0.0, tb = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.mwbase = mwbase
		self.tp = tp
		self.ke = ke
		self.tip = tip
		self.tdp = tdp
		self.tfp = tfp
		self.tf = tf
		self.kfcor = kfcor
		self.db1 = db1
		self.wfmax = wfmax
		self.wfmin = wfmin
		self.pmax = pmax
		self.ten = ten
		self.tw = tw
		self.kwcor = kwcor
		self.db2 = db2
		self.wwmax = wwmax
		self.wwmin = wwmin
		self.wmax1 = wmax1
		self.wmax2 = wmax2
		self.tvhp = tvhp
		self.cho = cho
		self.chc = chc
		self.hhpmax = hhpmax
		self.tvip = tvip
		self.cio = cio
		self.cic = cic
		self.simx = simx
		self.thp = thp
		self.trh = trh
		self.tlp = tlp
		self.prhmax = prhmax
		self.khp = khp
		self.klp = klp
		self.tb = tb
		
	def __str__(self):
		str = 'class=GovSteamEU\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
