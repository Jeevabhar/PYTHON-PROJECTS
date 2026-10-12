members=["keerthi","jeeva","ramu","somu","deepa"]
firstmembers=[0]
lastmembers=[-1]
members.append("prem")
members.insert(1,"prem")
members.remove("keerthi")
members.pop(2)
total_members = len(members)
print(members)
print(total_members)
print("welcome keerthi, jeeva ,ramu, somu, deepa")
club=("west","Mambalam","chennai")
print(club)
unique_program={"heart","lungs","neck"}
print(unique_program)
unique_program=len(unique_program)
print(f"no of unique program{unique_program}")
morning_members=["keerthi","jeeva","ramu"]
print(f"morning batch,{members}")
evening_members=["somu","deepa","prem"]
print(f"evening batch,{members}")
all_program=morning_members+evening_members
unique_program=set(all_program)
print("---unique program Names---")
print(unique_program)


