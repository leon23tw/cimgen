from cimpy.cimgen_v2_4_15_flat_9.IdentifiedObject import IdentifiedObject


class Diagram(IdentifiedObject):
	'''
	The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation.

	:DiagramStyle: A Diagram may have a DiagramStyle. Default: None
	:orientation: Coordinate system orientation of the diagram. Default: None
	:x1InitialView: X coordinate of the first corner of the initial view. Default: 0.0
	:x2InitialView: X coordinate of the second corner of the initial view. Default: 0.0
	:y1InitialView: Y coordinate of the first corner of the initial view. Default: 0.0
	:y2InitialView: Y coordinate of the second corner of the initial view. Default: 0.0
	:DiagramElements: A diagram is made up of multiple diagram objects. Default: []
		'''

	possibleProfileList = {'class': ['DI', ],
						'DiagramStyle': ['DI', ],
						'orientation': ['DI', ],
						'x1InitialView': ['DI', ],
						'x2InitialView': ['DI', ],
						'y1InitialView': ['DI', ],
						'y2InitialView': ['DI', ],
						'DiagramElements': ['DI', ],
												}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, DiagramStyle = None, orientation = None, x1InitialView = 0.0, x2InitialView = 0.0, y1InitialView = 0.0, y2InitialView = 0.0, DiagramElements = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DiagramStyle = DiagramStyle
		self.orientation = orientation
		self.x1InitialView = x1InitialView
		self.x2InitialView = x2InitialView
		self.y1InitialView = y1InitialView
		self.y2InitialView = y2InitialView
		self.DiagramElements = DiagramElements
		
	def __str__(self):
		str = 'class=Diagram\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
