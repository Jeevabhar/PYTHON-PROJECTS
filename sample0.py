def calculate_BMI(height,weight):
    return weight/(height*2)

def membership_message(name,program="generalfitness"):
        
        return f"{name}isenrolledin{program}"

def calculate_total_sessions(sessions_per_week,week):
    return sessions_per_week*week

def total_minutes_4_weeks(weekly_minutes):
    return weekly_minutes*4

bmi=calculate_BMI(70,166)
print(f"BMI:{bmi:2f}")

print(membership_message("kaviya"))
print(membership_message("ravi","yoga training"))

total=calculate_total_sessions(5,4)
print(f"Total sessions:{total}")

minutes=total_minutes_4_weeks(150)
print(f"Total minutes in 4 weeks:{minutes}")
      
    