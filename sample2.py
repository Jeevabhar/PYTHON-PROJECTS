name=str(input("enter the memeber name"))
age=int(input("enter the age"))
price=float(input("enter the price per session"))
session=int(input("enter the number of session "))
calories=int(input("enter the calories burned per session"))
total_cost=price*session
total_calories=calories*session
avg_calories=total_calories/session
membership_amount= 200
full_amount=total_cost
discount_amount=membership_amount
final_amount=full_amount
final_amount-=membership_amount
if age>=18:
    print("adult age")
elif total_cost>=2000:
  print("is expensive")
elif avg_calories>=300:
  print("high calories")
print(f"-----fittness summary------")
print(f"name:{name}")
print(f"final amount:{final_amount}") 
    
    










