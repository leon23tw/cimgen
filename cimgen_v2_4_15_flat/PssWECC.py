from cimpy.cimgen_v2_4_15_flat_9.PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


class PssWECC(PowerSystemStabilizerDynamics):
	'''
	Dual input Power System Stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western Electricity Coordinating Council, USA).

	:inputSignal1Type: Type of input signal #1. Default: None
	:inputSignal2Type: Type of input signal #2. Default: None
	:k1: Input signal 1 gain  (K). Default: 0.0
	:t1: Input signal 1 transducer time constant (T). Default: 0.0
	:k2: Input signal 2 gain (K). Default: 0.0
	:t2: Input signal 2 transducer time constant (T). Default: 0.0
	:t3: Stabilizer washout time constant (T). Default: 0.0
	:t4: Stabilizer washout time lag constant (T) (>0). Default: 0.0
	:t5: Lead time constant (T). Default: 0.0
	:t6: Lag time constant (T). Default: 0.0
	:t7: Lead time constant (T). Default: 0.0
	:t8: Lag time constant (T). Default: 0.0
	:t10: Lag time constant (T). Default: 0.0
	:t9: Lead time constant (T). Default: 0.0
	:vsmax: Maximum output signal (Vsmax). Default: 0.0
	:vsmin: Minimum output signal (Vsmin). Default: 0.0
	:vcu: Maximum value for voltage compensator output (V). Default: 0.0
	:vcl: Minimum value for voltage compensator output (V). Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'inputSignal1Type': ['DY', ],
						'inputSignal2Type': ['DY', ],
						'k1': ['DY', ],
						't1': ['DY', ],
						'k2': ['DY', ],
						't2': ['DY', ],
						't3': ['DY', ],
						't4': ['DY', ],
						't5': ['DY', ],
						't6': ['DY', ],
						't7': ['DY', ],
						't8': ['DY', ],
						't10': ['DY', ],
						't9': ['DY', ],
						'vsmax': ['DY', ],
						'vsmin': ['DY', ],
						'vcu': ['DY', ],
						'vcl': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class PowerSystemStabilizerDynamics: \n' + PowerSystemStabilizerDynamics.__doc__ 

	def __init__(self, inputSignal1Type = None, inputSignal2Type = None, k1 = 0.0, t1 = 0.0, k2 = 0.0, t2 = 0.0, t3 = 0.0, t4 = 0.0, t5 = 0.0, t6 = 0.0, t7 = 0.0, t8 = 0.0, t10 = 0.0, t9 = 0.0, vsmax = 0.0, vsmin = 0.0, vcu = 0.0, vcl = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.inputSignal1Type = inputSignal1Type
		self.inputSignal2Type = inputSignal2Type
		self.k1 = k1
		self.t1 = t1
		self.k2 = k2
		self.t2 = t2
		self.t3 = t3
		self.t4 = t4
		self.t5 = t5
		self.t6 = t6
		self.t7 = t7
		self.t8 = t8
		self.t10 = t10
		self.t9 = t9
		self.vsmax = vsmax
		self.vsmin = vsmin
		self.vcu = vcu
		self.vcl = vcl
		
	def __str__(self):
		str = 'class=PssWECC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
