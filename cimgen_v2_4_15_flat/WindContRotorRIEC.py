from cimpy.cimgen_v2_4_15_flat_9.IdentifiedObject import IdentifiedObject


class WindContRotorRIEC(IdentifiedObject):
	'''
	Rotor resistance control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.2.

	:kirr: Integral gain in rotor resistance PI controller (). It is type dependent parameter. Default: 0.0
	:komegafilt: Filter gain for generator speed measurement (K). It is type dependent parameter. Default: 0.0
	:kpfilt: Filter gain for power measurement (). It is type dependent parameter. Default: 0.0
	:kprr: Proportional gain in rotor resistance PI controller (). It is type dependent parameter. Default: 0.0
	:rmax: Maximum rotor resistance (). It is type dependent parameter. Default: 0.0
	:rmin: Minimum rotor resistance (). It is type dependent parameter. Default: 0.0
	:tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0.0
	:tpfilt: Filter time constant for power measurement (). It is type dependent parameter. Default: 0.0
	:WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model. Default: []
	:WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is associated. Default: None
		'''

	possibleProfileList = {'class': ['DY', ],
						'kirr': ['DY', ],
						'komegafilt': ['DY', ],
						'kpfilt': ['DY', ],
						'kprr': ['DY', ],
						'rmax': ['DY', ],
						'rmin': ['DY', ],
						'tomegafilt': ['DY', ],
						'tpfilt': ['DY', ],
						'WindDynamicsLookupTable': ['DY', ],
						'WindGenTurbineType2IEC': ['DY', ],
												}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, kirr = 0.0, komegafilt = 0.0, kpfilt = 0.0, kprr = 0.0, rmax = 0.0, rmin = 0.0, tomegafilt = 0.0, tpfilt = 0.0, WindDynamicsLookupTable = [], WindGenTurbineType2IEC = None,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.kirr = kirr
		self.komegafilt = komegafilt
		self.kpfilt = kpfilt
		self.kprr = kprr
		self.rmax = rmax
		self.rmin = rmin
		self.tomegafilt = tomegafilt
		self.tpfilt = tpfilt
		self.WindDynamicsLookupTable = WindDynamicsLookupTable
		self.WindGenTurbineType2IEC = WindGenTurbineType2IEC
		
	def __str__(self):
		str = 'class=WindContRotorRIEC\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
