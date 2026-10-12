name=str(input("enter the name"))
age=int(input("enter the age"))
weight=float(input("enter the weight in kg"))
height=float(input("enter the height in m"))
goal_weight=float(input("enter the goal weight in kg"))
current_weight=float(input("enter the current weight in kg"))
bmi =weight/(height**2)
print("------fitness profile-------")
print("name",name)
print("age",age)
print("weight",weight)
print("height",height)
print("---------goal_weight------")
weight_to_lose=current_weight-goal_weight
print("goalweight",goal_weight)
print("weighttolose",weight_to_lose)



