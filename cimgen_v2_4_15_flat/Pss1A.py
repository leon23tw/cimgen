from cimpy.cimgen_v2_4_15_flat_9.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class Pss1A(PowerSystemStabilizerDynamics):
	'''
	Single input power system stabilizer. It is a modified version in order to allow representation of various vendors' implementations on PSS type 1A.

	:inputSignalType: Type of input signal. Default: None
	:a1: Notch filter parameter (A1). Default: 0.0
	:a2: Notch filter parameter (A2). Default: 0.0
	:t1: Lead/lag time constant (T1). Default: 0.0
	:t2: Lead/lag time constant (T2). Default: 0.0
	:t3: Lead/lag time constant (T3). Default: 0.0
	:t4: Lead/lag time constant (T4). Default: 0.0
	:t5: Washout time constant (T5). Default: 0.0
	:t6: Transducer time constant (T6). Default: 0.0
	:ks: Stabilizer gain (Ks). Default: 0.0
	:vrmax: Maximum stabilizer output (Vrmax). Default: 0.0
	:vrmin: Minimum stabilizer output (Vrmin). Default: 0.0
	:vcu: Stabilizer input cutoff threshold (Vcu). Default: 0.0
	:vcl: Stabilizer input cutoff threshold (Vcl). Default: 0.0
	:a3: Notch filter parameter (A3). Default: 0.0
	:a4: Notch filter parameter (A4). Default: 0.0
	:a5: Notch filter parameter (A5). Default: 0.0
	:a6: Notch filter parameter (A6). Default: 0.0
	:a7: Notch filter parameter (A7). Default: 0.0
	:a8: Notch filter parameter (A8). Default: 0.0
	:kd: Selector (Kd).  true = e used false = e not used. Default: False
	:tdelay: Time constant (Tdelay). Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'inputSignalType': ['DY', ],
						'a1': ['DY', ],
						'a2': ['DY', ],
						't1': ['DY', ],
						't2': ['DY', ],
						't3': ['DY', ],
						't4': ['DY', ],
						't5': ['DY', ],
						't6': ['DY', ],
						'ks': ['DY', ],
						'vrmax': ['DY', ],
						'vrmin': ['DY', ],
						'vcu': ['DY', ],
						'vcl': ['DY', ],
						'a3': ['DY', ],
						'a4': ['DY', ],
						'a5': ['DY', ],
						'a6': ['DY', ],
						'a7': ['DY', ],
						'a8': ['DY', ],
						'kd': ['DY', ],
						'tdelay': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignalType = None, a1 = 0.0, a2 = 0.0, t1 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, ks = 0.0, vrmax = 0.0, vrmin = 0.0, vcu = 0.0, vcl = 0.0, a3 = 0.0, a4 = 0.0, a5 = 0.0, a6 = 0.0, a7 = 0.0, a8 = 0.0, kd = False, tdelay = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignalType = inputSignalType
		self.a1 = a1
		self.a2 = a2
		self.t1 = t1
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.ks = ks
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.vcu = vcu
		self.vcl = vcl
		self.a3 = a3
		self.a4 = a4
		self.a5 = a5
		self.a6 = a6
		self.a7 = a7
		self.a8 = a8
		self.kd = kd
		self.tdelay = tdelay
		
	def __str__(self):
		str = 'class=Pss1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
