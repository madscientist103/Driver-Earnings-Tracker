import csv
import datetime
import daily_entry_object
import profile_stats

def main():

	running = 1
	
	#current_profile = "new_profile"
	current_file = "profile.csv"
	
	entry_list = dict()
	
	user_profile_stats = profile_stats.Profile_Stats() 
	
	try:
		#f = open(current_file, "x")
		
		with open(current_file, 'w', newline='') as csvfile:
			fieldnames = ['date', 'day_of_week', 'start_time', 'end_time']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
			writer.writeheader()
			
	except FileExistsError:
		print("profile already exists!")
	
	#with open(current_file, newline='') as csvfile:
		#reader = csv.DictReader(csvfile)
		#for row in reader:
			#print(row['start_time'], row['end_time'])
			
	
		
	
	while (running):
		menu(current_file, entry_list, user_profile_stats)
		
def menu(current_file, entry_list, user_profile_stats):

	while(True):
	
		user_profile_stats = calculate_stats(user_profile_stats, entry_list)
	
		print("\nCURRENT PROFILE:", current_file)

		print("\n********MENU********\n")
		print("1. Stats")
		print("2. Add Entry")
		print("3. Report")
		print("4. Export Report")
		print("5. Quit\n")
	
		user_selection = int(input("\nPlease enter your selection:"))
	
		print("\n*****************************************\n")
	
		
			
		if user_selection == 1:
		
			show_quick_stats(user_profile_stats)
		
		elif user_selection == 2:
			entry_list = add_entry(entry_list)
		
		elif user_selection == 3:
			show_entry_report(entry_list)

		elif user_selection == 4:
			print("\nFunctionality Pending...\n")

		elif user_selection == 5:
			exit()
		
		else:
			print("\nSorry, not a valid selection, please try again...\n")

def add_entry_date():

	print("\n*****************************************\n")

	date_year_input_run = 1
	date_month_input_run = 1
	date_day_input_run = 1
	
	while date_year_input_run == 1:
		date_year = int(input("\nPlease enter the numeric year:	"))
		
		if date_year <= 0:
			print("\nSorry, not a valid year!")
		
		else:
			date_year_input_run = 0
			
	while date_month_input_run == 1:
		date_month = int(input("\nPlease enter the numeric month 1-12:	"))
		
		if date_month <= 0 or date_month > 12:
			print("\nSorry, not a valid month. Must be an integer value between 1 and 12 representing the month.")
			
		else:
			date_month_input_run = 0
			
	while date_day_input_run == 1:
		date_day = int(input("\nPlease enter the numeric day 1-31:	"))
		
		if date_day <= 0 or date_day > 31:
			print("\nSorry, not a valid day. Must be an integer value between 1 and 31.")
			
		else:
			date_day_input_run = 0
	try:		
		entry_date = datetime.datetime(date_year, date_month, date_day)
		
	except ValueError:
		print("\nThe day you entered is out of range for the given month. Using default.")
		entry_date = datetime.datetime(2020, 1, 1)	
			
	print("\nThe date entered is:	", entry_date.strftime("%A"), entry_date.strftime("%B"), entry_date.strftime("%d"), entry_date.strftime("%Y"))
	
	print("\n*****************************************\n")
		
		
	return entry_date
	
def start_time(entry_date):

	print("\n*****************************************\n")

	time_format = "%H:%M"

	start_hour_input_run = 1
	start_minute_input_run = 1
	
	while start_hour_input_run == 1:
		start_hour = int(input("\nEnter the start hour in military format XX:	"))
		
		if start_hour < 0 or start_hour > 23:
			print("\nStart hour must be between 0 and 24.")
			
		else:
			start_hour_input_run = 0
			
	while start_minute_input_run == 1:
		start_minute = int(input("\nEnter the start minutes in XX format, example '23':	"))
		
		if start_minute < 0 or start_minute > 59:
			print("\nMinutes must be between 0 and 59.")
			
		else:
			start_minute_input_run = 0
	
	#extracting entry date components
	entry_date_year = int(entry_date.strftime("%Y"))
	entry_date_month = int(entry_date.strftime("%m"))
	entry_date_day = int(entry_date.strftime("%d"))
	
	start_time = datetime.datetime(entry_date_year, entry_date_month, entry_date_day, start_hour, start_minute)
	print("\nThe start time you have entered is:	", start_time.strftime(time_format))
	
	print("\n*****************************************\n")
			
	return start_time
	
def end_time(entry_start_time):

	print("\n*****************************************\n")

	time_format = "%H:%M"
	
	#extracting entry date components
	entry_date_year = int(entry_start_time.strftime("%Y"))
	entry_date_month = int(entry_start_time.strftime("%m"))
	entry_date_day = int(entry_start_time.strftime("%d"))
	start_hour = int(entry_start_time.strftime("%H"))

	end_hour_input_run = 1
	end_minute_input_run = 1
	
	while end_hour_input_run == 1:
		end_hour = int(input("\nEnter the end hour in military format:	"))
		
		if end_hour < 0 or end_hour > 23:
			print("\nEnd hour must be between 0 and 24.")
			
		if end_hour < start_hour:
			print("\nEnd hour cannot be before start hour.")
			
		else:
			end_hour_input_run = 0
			
	while end_minute_input_run == 1:
		end_minute = int(input("\nEnter the shift end minutes, example '23':	"))
		
		if end_minute < 0 or end_minute > 59:
			print("\nMinutes must be between 0 and 59.")
			
		else:
			end_minute_input_run = 0
	
	
	
	end_time = datetime.datetime(entry_date_year, entry_date_month, entry_date_day, end_hour, end_minute)
	print("\nThe end time you have entered is:	", end_time.strftime(time_format))
	
	print("\n*****************************************\n")
			
	return end_time
	
	
	
def calculate_shift_duration(start_time, end_time):

	shift_duration = end_time - start_time
	
	return shift_duration
	
def lunch_start_time(entry_start_time, entry_end_time, entry_date):

	print("\n*****************************************\n")

	time_format = "%H:%M"

	
	lunch_start_time_validation = 1
	
	while(lunch_start_time_validation == 1):
	
		lunch_start_hour_input_run = 1
		lunch_start_minute_input_run = 1
	
		while lunch_start_hour_input_run == 1:
			lunch_start_hour = int(input("\nEnter the lunch start hour in military format XX:	"))
		
			if lunch_start_hour < 0 or lunch_start_hour > 23:
				print("\nLunch start hour must be between 0 and 24.")
			
		#if lunch_start_hour < entry_start_time or lunch_start_hour > entry_end_time:
			#print("\nLunch start hour cannot be less than shift start time or greater than shift end time.")
			
			else:
				lunch_start_hour_input_run = 0
			
		while lunch_start_minute_input_run == 1:
			lunch_start_minute = int(input("\nEnter the lunch start minutes in XX format, example '23':	"))
		
			if lunch_start_minute < 0 or lunch_start_minute > 59:
				print("\nLunch start minutes must be between 0 and 59.")
			
			else:
				lunch_start_minute_input_run = 0
	
		#extracting entry date components
		entry_date_year = int(entry_date.strftime("%Y"))
		entry_date_month = int(entry_date.strftime("%m"))
		entry_date_day = int(entry_date.strftime("%d"))
	
		lunch_start_time = datetime.datetime(entry_date_year, entry_date_month, entry_date_day, lunch_start_hour, lunch_start_minute)
	
	
	
		if lunch_start_time < entry_start_time or lunch_start_time > entry_end_time:
		
			print("\nLunch start time cannot be less than shift start time or greater than shift end time.")
			
		else:
		
			print("\nThe lunch start time you have entered is:	", lunch_start_time.strftime(time_format))
			
			lunch_start_time_validation = 0
	
	print("\n*****************************************\n")
			
	return lunch_start_time
	
def lunch_end_time(entry_start_time, entry_end_time, lunch_start_time, entry_date):

	print("\n*****************************************\n")

	time_format = "%H:%M"

	
	lunch_end_time_validation = 1
	
	while(lunch_end_time_validation == 1):
	
		lunch_end_hour_input_run = 1
		lunch_end_minute_input_run = 1
	
		while lunch_end_hour_input_run == 1:
			lunch_end_hour = int(input("\nEnter the lunch end hour in military format XX:	"))
		
			if lunch_end_hour < 0 or lunch_end_hour > 23:
				print("\nLunch end hour must be between 0 and 24.")
			
			
			else:
				lunch_end_hour_input_run = 0
			
		while lunch_end_minute_input_run == 1:
			lunch_end_minute = int(input("\nEnter the lunch end minutes in XX format, example '23':	"))
		
			if lunch_end_minute < 0 or lunch_end_minute > 59:
				print("\nLunch end minutes must be between 0 and 59.")
			
			else:
				lunch_end_minute_input_run = 0
	
		#extracting entry date components
		entry_date_year = int(entry_date.strftime("%Y"))
		entry_date_month = int(entry_date.strftime("%m"))
		entry_date_day = int(entry_date.strftime("%d"))
	
		lunch_end_time = datetime.datetime(entry_date_year, entry_date_month, entry_date_day, lunch_end_hour, lunch_end_minute)
	
	
	
		if lunch_end_time < entry_start_time or lunch_end_time > entry_end_time:
		
			print("\nLunch end time cannot be less than shift start time or greater than shift end time.")
			
		elif lunch_end_time < lunch_start_time:
		
			print("\nLunch end time cannot be less than lunch start time.")
			
		else:
		
			print("\nThe lunch end time you have entered is:	", lunch_end_time.strftime(time_format))
			
			lunch_end_time_validation = 0
	
	print("\n*****************************************\n")
			
	return lunch_end_time
	
def calculate_lunch_duration(lunch_start_time, lunch_end_time):

	lunch_duration = lunch_end_time - lunch_start_time
	
	return lunch_duration
	
def add_entry(entry_list):

	print("\n*******Adding a New Entry********\n")

	#the date of the entry.
	entry_date = add_entry_date()
	
	#calculate shift start, end and duration.
	entry_start_time = start_time(entry_date)
	entry_end_time = end_time(entry_start_time)
	entry_shift_duration = calculate_shift_duration(entry_start_time, entry_end_time)
	print("\nThe shift duration is:", entry_shift_duration, "hours.")
	entry_shift_duration_value = entry_shift_duration.seconds/3600
	
	#calculate the shift lunch start, end, and duration.
	entry_lunch_start_time = lunch_start_time(entry_start_time, entry_end_time, entry_date)
	entry_lunch_end_time = lunch_end_time(entry_start_time, entry_end_time, entry_lunch_start_time, entry_date)
	entry_lunch_duration = calculate_lunch_duration(entry_lunch_start_time, entry_lunch_end_time)
	print("\nThe shift lunch duration is:", entry_lunch_duration, "hours.")
	entry_lunch_duration_value = entry_lunch_duration.seconds/3600
	
	#calculate the total hours worked
	hours_worked = entry_shift_duration_value - entry_lunch_duration_value
	print("\nYou worked", hours_worked, "hours this shift.")
	
	#calculate the fuel usage based upon miles and mpg.
	print("\n*****************************************\n")
	miles = float(input("\nEnter the total miles driven for this day:	"))
	mpg = float(input("\nEnter the average mpg for your vehicle:	"))
	gallons_used = float(miles/mpg)
	print("\nYou used", "{:10.2f}".format(gallons_used), "gallons of fuel this day.")
	print("\n*****************************************\n")
	
	#calculate the fuel cost
	print("\n*****************************************\n")
	fuel_price = float(input("\nEnter your cost of fuel:	"))
	fuel_cost = fuel_price * gallons_used
	print("\nYou spent", "{:10.2f}".format(fuel_cost), "dollars on fuel this day.")
	print("\n*****************************************\n")
	
	#calculate the gross income based on fare and tips.
	print("\n*****************************************\n")
	fare = float(input("\nEnter the fare received for this day:	"))
	tips = float(input("\nEnter the tips received for this day:	"))
	gross_earnings = fare + tips
	print("\nYour gross earnings are", "{:10.2f}".format(gross_earnings), "dollars.")
	print("\n*****************************************\n")
	
	#calculate net earnings based on expenses.
	print("\n*****************************************\n")
	net_earnings = gross_earnings - fuel_cost
	print("\nYour net earnings after fuel expense are", "{:10.2f}".format(net_earnings), "dollars.")
	
	#calculate the hourly rate.
	hourly_rate = net_earnings/hours_worked
	print("\nYour hourly rate is", "{:10.2f}".format(hourly_rate), "dollars per hour.")
	
	#initialize daily entry object with entry date. Each entry object must have a unique entry date.
	daily_entry = daily_entry_object.Daily_Entry_Object(entry_date)
	daily_entry.shift_start_time = entry_start_time
	daily_entry.shift_end_time = entry_end_time
	daily_entry.shift_lunch_start_time = entry_lunch_start_time
	daily_entry.shift_lunch_end_time = entry_lunch_end_time
	daily_entry.shift_duration = entry_shift_duration
	daily_entry.shift_lunch_duration = entry_lunch_duration
	daily_entry.shift_hours_worked = hours_worked
	daily_entry.miles = miles
	daily_entry.mpg = mpg
	daily_entry.gallons_used = gallons_used 
	daily_entry.fuel_price = fuel_price
	daily_entry.fuel_cost = fuel_cost
	daily_entry.fare = fare
	daily_entry.tips = tips
	daily_entry.gross_earnings = gross_earnings
	daily_entry.net_earnings = net_earnings
	daily_entry.hourly_rate = hourly_rate
	entry_list[entry_date] = daily_entry
	
	return entry_list
	
def show_entry_report(entry_list):

	time_format = "%H:%M"

	sorted_entry_list = {key: val for key, val in sorted(entry_list.items(), key = lambda ele: ele[0])}

	for date in sorted_entry_list:
	
		print("\n*******Showing info for entry:", sorted_entry_list[date].entry_date.strftime("%A, %B %d, %Y"))
		print("Shift Start Time:", sorted_entry_list[date].shift_start_time.strftime(time_format))
		print("Shift End Time:", sorted_entry_list[date].shift_end_time.strftime(time_format))
		print("Shift Duration:", sorted_entry_list[date].shift_duration)
		print("Shift Lunch Start Time:", sorted_entry_list[date].shift_lunch_start_time.strftime(time_format))
		print("Shift Lunch End Time:", sorted_entry_list[date].shift_lunch_end_time.strftime(time_format))
		print("Shift Lunch Duration:", sorted_entry_list[date].shift_lunch_duration)
		print("Shift Hours Worked:", sorted_entry_list[date].shift_hours_worked)
		print("Miles Driven:", sorted_entry_list[date].miles)
		print("MPG for Shift:", sorted_entry_list[date].mpg)
		print("Gallons of Fuel Used:", sorted_entry_list[date].gallons_used)
		print("Fuel Price Paid:", sorted_entry_list[date].fuel_price)
		print("Fuel Expense for Shift:", sorted_entry_list[date].fuel_cost)
		print("Fare Received for Shift:", sorted_entry_list[date].fare)
		print("Tips received for shift:", sorted_entry_list[date].tips)
		print("Gross Earnings for Shift:", sorted_entry_list[date].gross_earnings)
		print("Net Earnings for Shift:", sorted_entry_list[date].net_earnings)
		print("Average Hourly Rate for Shift:", sorted_entry_list[date].hourly_rate)
		print("**********************************\n")
		
def show_quick_stats(user_profile_stats):

	print("\nNumber of work days in profile....:", user_profile_stats.num_days) 
	print("Total number of hours worked......:", user_profile_stats.hours_worked_sum) 
	print("Total number of lunch hours.......:", user_profile_stats.lunch_duration_sum)
	print("Average shift duration:...........:", user_profile_stats.av_shift_duration)
	print("Average Fare per shift:...........:", user_profile_stats.av_fare)
	print("Average lunch shift duration:.....:", user_profile_stats.av_lunch_duration)
	print("Total fare received:..............:", user_profile_stats.total_fare)
	print("Average hours worked:.............:", user_profile_stats.av_hours_worked)
	print("Average tips per shift:...........:", user_profile_stats.av_tips)
	print("Average miles driven:.............:", user_profile_stats.av_miles)
	print("Total tips received...............:", user_profile_stats.total_tips)
	print("Total Miles Driven:...............:", user_profile_stats.total_miles_driven)
	print("Average gross earnings............:", user_profile_stats.av_gross)
	print("Average MPG:......................:", user_profile_stats.av_mpg)
	print("Total gross earnings..............:", user_profile_stats.total_gross)
	print("Average fuel use:.................:", user_profile_stats.av_fuel_use)
	print("Average net earnings..............:", user_profile_stats.av_net)
	print("Total gallons of fuel used:.......:", user_profile_stats.total_fuel_use)
	print("Average hourly rate...............:", user_profile_stats.av_hourly_rate)
	print("Average fuel price paid:..........:", user_profile_stats.av_fuel_price)
	print("Average fuel expense per shift....:", user_profile_stats.av_fuel_expense)
	print("Total fuel expense................:", user_profile_stats.total_fuel_use)
	

def calculate_stats(user_profile_stats, entry_list):

	shift_duration_sum = 0
	lunch_duration_sum = 0
	hours_worked_sum = 0
	miles_driven_sum = 0
	fare_earned_sum = 0
	tips_earned_sum = 0
	gross_earnings_sum = 0
	mpg_sum = 0
	fuel_use_sum = 0
	net_earnings_sum = 0
	hourly_rate_sum = 0
	fuel_price_sum = 0
	fuel_expense_sum = 0
	entry_list_length = len(entry_list)

	for index, date in enumerate(entry_list):
	
		shift_duration_sum = shift_duration_sum + entry_list[date].shift_duration.seconds/3600
		lunch_duration_sum = lunch_duration_sum + entry_list[date].shift_lunch_duration.seconds/3600
		hours_worked_sum = hours_worked_sum + entry_list[date].shift_hours_worked
		miles_driven_sum = miles_driven_sum + entry_list[date].miles
		fare_earned_sum = fare_earned_sum + entry_list[date].fare
		tips_earned_sum = tips_earned_sum + entry_list[date].tips
		gross_earnings_sum = gross_earnings_sum + entry_list[date].gross_earnings
		mpg_sum = mpg_sum + entry_list[date].mpg
		fuel_use_sum = fuel_use_sum + entry_list[date].gallons_used
		net_earnings_sum = net_earnings_sum + entry_list[date].net_earnings
		hourly_rate_sum = hourly_rate_sum + entry_list[date].hourly_rate
		fuel_price_sum = fuel_price_sum + entry_list[date].fuel_price
		fuel_expense_sum = fuel_expense_sum + entry_list[date].fuel_cost
	
	if entry_list_length > 0:
	
		av_shift_duration = float(shift_duration_sum/entry_list_length)
		av_lunch_duration = float(lunch_duration_sum/entry_list_length)
		av_hours_worked = float(hours_worked_sum/entry_list_length)
		av_miles_driven = float(miles_driven_sum/entry_list_length)
		av_fare_earned = float(fare_earned_sum/entry_list_length)
		av_tips_earned = float(tips_earned_sum/entry_list_length)
		av_gross_earnings = float(gross_earnings_sum/entry_list_length)
		av_mpg = float(mpg_sum/entry_list_length)
		av_fuel_use = float(fuel_use_sum/entry_list_length)
		av_net_earnings = float(net_earnings_sum/entry_list_length)
		av_hourly_rate = float(hourly_rate_sum/entry_list_length)
		av_fuel_price = float(fuel_price_sum/entry_list_length)
		av_fuel_expense = float(fuel_expense_sum/entry_list_length)
				
	else:
	
		av_shift_duration = 0
		av_lunch_duration = 0
		av_hours_worked = 0
		av_miles_driven = 0
		av_fare_earned = 0
		av_tips_earned = 0
		av_gross_earnings = 0
		av_mpg = 0
		av_fuel_use = 0
		av_net_earnings = 0
		av_hourly_rate = 0
		av_fuel_price = 0
		av_fuel_expense = 0
		
	#print("shift duration sum is:", shift_duration_sum)
	#print("number of days worked:", entry_list_length)
	#print("average shift durastion:", av_shift_duration)
	
	user_profile_stats.num_days = entry_list_length
	user_profile_stats.shift_duration_sum = shift_duration_sum
	user_profile_stats.av_shift_duration = av_shift_duration
	user_profile_stats.lunch_duration_sum = lunch_duration_sum
	user_profile_stats.av_lunch_duration = av_lunch_duration
	user_profile_stats.hours_worked_sum = hours_worked_sum
	user_profile_stats.av_hours_worked = av_hours_worked
	user_profile_stats.total_miles_driven = miles_driven_sum
	user_profile_stats.av_miles = av_miles_driven
	user_profile_stats.av_fare = av_fare_earned
	user_profile_stats.total_fare = fare_earned_sum
	user_profile_stats.total_tips = tips_earned_sum
	user_profile_stats.av_tips = av_tips_earned
	user_profile_stats.total_gross = gross_earnings_sum
	user_profile_stats.av_gross = av_gross_earnings
	user_profile_stats.av_mpg = av_mpg
	user_profile_stats.total_fuel_use = fuel_use_sum
	user_profile_stats.av_fuel_use = av_fuel_use
	user_profile_stats.total_net = net_earnings_sum
	user_profile_stats.av_net = av_net_earnings
	user_profile_stats.av_hourly_rate = av_hourly_rate
	user_profile_stats.av_fuel_price = av_fuel_price
	user_profile_stats.av_fuel_expense = av_fuel_expense

	return user_profile_stats
	
main()
