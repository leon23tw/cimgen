from cimpy.cimgen_v2_4_15_flat_9.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcDC1A(ExcitationSystemDynamics):
	'''
	Modified IEEE DC1A direct current commutator exciter with speed input and without underexcitation limiters (UEL) inputs.

	:ka: Voltage regulator gain (Ka).  Typical Value = 46. Default: 0.0
	:ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0. Default: 0.0
	:ta: Voltage regulator time constant (Ta).  Typical Value = 0.06. Default: 0.0
	:tb: Voltage regulator time constant (Tb).  Typical Value = 0. Default: 0.0
	:tc: Voltage regulator time constant (Tc).  Typical Value = 0. Default: 0.0
	:vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1. Default: 0.0
	:vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -0.9. Default: 0.0
	:ke: Exciter constant related to self-excited field (Ke).  Typical Value = 0. Default: 0.0
	:te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.46. Default: 0.0
	:kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1. Default: 0.0
	:tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1. Default: 0.0
	:efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 3.1. Default: 0.0
	:seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.33. Default: 0.0
	:efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 2.3. Default: 0.0
	:seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value = 0.33. Default: 0.0
	:exclim: (exclim). IEEE standard is ambiguous about lower limit on exciter output.  true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
	:efdmin: Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99. Default: 0.0
	:edfmax: Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99. Default: 0.0
		'''

	possibleProfileList = {'class': ['DY', ],
						'ka': ['DY', ],
						'ks': ['DY', ],
						'ta': ['DY', ],
						'tb': ['DY', ],
						'tc': ['DY', ],
						'vrmax': ['DY', ],
						'vrmin': ['DY', ],
						'ke': ['DY', ],
						'te': ['DY', ],
						'kf': ['DY', ],
						'tf': ['DY', ],
						'efd1': ['DY', ],
						'seefd1': ['DY', ],
						'efd2': ['DY', ],
						'seefd2': ['DY', ],
						'exclim': ['DY', ],
						'efdmin': ['DY', ],
						'edfmax': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class ExcitationSystemDynamics: \n' + ExcitationSystemDynamics.__doc__ 

	def __init__(self, ka = 0.0, ks = 0.0, ta = 0.0, tb = 0.0, tc = 0.0, vrmax = 0.0, vrmin = 0.0, ke = 0.0, te = 0.0, kf = 0.0, tf = 0.0, efd1 = 0.0, seefd1 = 0.0, efd2 = 0.0, seefd2 = 0.0, exclim = False, efdmin = 0.0, edfmax = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.ka = ka
		self.ks = ks
		self.ta = ta
		self.tb = tb
		self.tc = tc
		self.vrmax = vrmax
		self.vrmin = vrmin
		self.ke = ke
		self.te = te
		self.kf = kf
		self.tf = tf
		self.efd1 = efd1
		self.seefd1 = seefd1
		self.efd2 = efd2
		self.seefd2 = seefd2
		self.exclim = exclim
		self.efdmin = efdmin
		self.edfmax = edfmax
		
	def __str__(self):
		str = 'class=ExcDC1A\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
