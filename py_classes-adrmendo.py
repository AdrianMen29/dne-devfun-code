class AccessPoint:
	"""AccessPoint Python class """
	def __init__(self, model, sw_version, ip_Addr,N_Radios):
		'''Initial Values'''
		self.model= model
		self.sw_version=sw_version
		self.ip_Addr=ip_Addr
		self.N_Radios=N_Radios

	def getDescription(self):
		"""Return a formatted Description of the AP"""
		dscpt= f'AccessPoint Model				:{self.model}\n'\
			   f'Software Version 				:{self.sw_version}\n'\
			   f'Mgmt IP Address  				:{self.ip_Addr}\'n'\
			   f'Number of Radios  				:{self.N_Radios}'
		return dscpt

# Filling the object
AP1=AccessPoint("AIR-AP3802I-E-K9","17.5.1","10.10.25.71",2)
AP2=AccessPoint("AIR-AP9120I-B-K9","17.5.1","10.10.25.72",3)

#showing the object
print("AP1\n",AP1.getDescription()," n\" , sep="")
print("AP2\n",AP2.getDescription(), "n\" , sep="")
