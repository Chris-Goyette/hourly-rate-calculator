# Calculator configuration 
number_of_paychecks_in_year = 24
number_of_hours_per_pay_period = 86.67

# Given annual salaries
annual_salary_90k = 90000
annual_salary_110k = 110000

# Calculating the gross hourly rate for both salaries using pay period details
hourly_rate_90k = annual_salary_90k / (number_of_paychecks_in_year * number_of_hours_per_pay_period)
hourly_rate_110k = annual_salary_110k / (number_of_paychecks_in_year * number_of_hours_per_pay_period)

# Print the calculated hourly rates
print(f"Hourly rate for $90,000 annual salary: ${hourly_rate_90k:.2f}")
print(f"Hourly rate for $110,000 annual salary: ${hourly_rate_110k:.2f}")

