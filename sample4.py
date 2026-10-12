score1 =float(input("enter the fitness score 1 :"))
score2 =float(input("enter the fitness score 2 :"))
score3 =float(input("enter the fitness score 3 :"))
scores =[score1,score2, score3]
total=0
for score  in  scores:
    total = total + score
    average=total/3
    print(f"total fitness score: {total}")
    print(f"average fitness score: {average:.2f}")p



           






