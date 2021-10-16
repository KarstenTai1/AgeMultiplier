user_age = int(input("What is your age? "))

age_in_years = str(user_age*1)
print("Your age in years : " + age_in_years)

age_in_months = user_age*12
print("Your age in months: " + str(age_in_months))

age_in_days = age_in_months*31
print("Your age in days: " + str(age_in_days))

age_in_hours = age_in_days*24
print("Your age in hours: " + str(age_in_hours))

age_in_minutes = age_in_hours*60
print("Your age in minutes: " + str(age_in_minutes))

age_in_seconds = age_in_minutes*60
print("Your age in seconds: " + str(age_in_seconds))

age_in_milaseconds = age_in_seconds*1000
print("Your age in milaseconds: " + str(age_in_milaseconds))



age_in_nanoseconds = age_in_milaseconds*1000000
print("Your age in nanoseconds: " + str(age_in_nanoseconds))