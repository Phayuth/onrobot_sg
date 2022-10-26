from pymodbus.client.sync import ModbusTcpClient as ModbusClient

class SG():

	def __init__(self, ip, port):
		self.client = ModbusClient(
			ip,
			port=port,
			stopbits=1,
			bytesize=8,
			parity='E',
			baudrate=115200,
			timeout=1)
		self.open_connection()

	def open_connection(self):
		"""Opens the connection with a gripper."""
		self.client.connect()

	def close_connection(self):
		"""Closes the connection with the gripper."""
		self.client.close()

	def set_target(self,command):
		"""
		Min = 10mm = 100
		Max = 75mm = 750
		"""
		if command < 110:
			command = 110
		elif command > 750:
			command = 750
			
		self.client.write_register(
			address=0x0000, value=command, unit=65)

	# def set_command(self,command):

	# 	self.client.write_register(
	# 		address=0x001, value=command, unit=65)

	def set_init(self):

		self.client.write_register(
			address=0x001, value=0x3, unit=65)
	
	def set_move(self):

		self.client.write_register(
			address=0x001, value=0x1, unit=65)

	def set_stop(self):

		self.client.write_register(
			address=0x001, value=0x2, unit=65)

	def set_gentle(self,command):
		"""
		True or False

		If true the gripping speed is reduced at 12.5mm before the specified target
		width, this results in a gentler grip, compared to normal grip settings.
		"""
		result = self.client.write_register(
			address=0x0002, value=command, unit=65)

	def set_model_id(self,type_id):

		result = self.client.write_register(
			address=0x0003, value=type_id, unit=65)

	def get_gp_wd(self):

		result = self.client.read_holding_registers(
			address=0x0100, count=1, unit=65)
		grip_p = result.registers[0]
		return grip_p

	def get_status(self):
	
		result = self.client.read_holding_registers(
			address=0x0103, count=1, unit=65)
		grip_p = result.registers[0]
		return grip_p

	def get_gp_max_wd(self):

		result = self.client.read_holding_registers(
			address=0x0105, count=1, unit=65)
		grip_p = result.registers[0]
		return grip_p

	def get_gp_min_wd(self):

		result = self.client.read_holding_registers(
			address=0x0106, count=1, unit=65)
		grip_p = result.registers[0]
		return grip_p