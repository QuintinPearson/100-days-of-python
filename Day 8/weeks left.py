weeks_in_year = 52
age = int(input("how old are you\n"))

def life_in_weeks(age):
    weeks_left = (90 * weeks_in_year) - (age * weeks_in_year)
    return print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(age)