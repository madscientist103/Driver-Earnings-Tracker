class Daily_Entry_Object:

	def __init__(self, entry_date):
	
		self.entry_date = entry_date
		self.shift_start_time = 0
		self.shift_end_time = 0
		self.shift_lunch_start_time = 0
		self.shift_lunch_end_time = 0
		self.shift_duration = self.shift_end_time - self.shift_start_time
		self.shift_lunch_duration = self.shift_lunch_end_time - self.shift_lunch_start_time
		self.shift_hours_worked = self.shift_duration - self.shift_lunch_duration
		self.miles = 0
		self.mpg = 0
		self.gallons_used = 0
		self.fuel_price = 0
		self.fuel_cost = 0
		self.fare = 0
		self.tips = 0
		self.gross_earnings = 0
		self.net_earnings = 0
		self.hourly_rate = 0
		
