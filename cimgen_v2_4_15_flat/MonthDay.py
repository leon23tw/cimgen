from cimpy.cimgen_v2_4_15_flat_9.Base import Base


class MonthDay(Base):
	'''
	MonthDay format as "--mm-dd", which conforms with XSD data type gMonthDay.

		'''

	possibleProfileList = {'class': ['EQ', ],
												}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=MonthDay\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
