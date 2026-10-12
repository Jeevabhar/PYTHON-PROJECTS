name=str(input("enter the memeber name"))
age=int(input("enter the age"))
fitness_level=str(input("enter the fitness level (beginner, intermediate, advanced):"))
member_status=str(input("are you memeber level (yes,no):"))
session=float(input("enter the number of session per week"))
##########AGE#########
if age<=18:
    print("junior finess level")
   ######### MEMBERSHIP########
else:
     print("please register for memebership")
     #########TRAINING LEVEL##########
     if age<=18:
          print("check the fitness level (beginner training level,intermediate training level, advanced training level):")
          ##########WEEKLY SESSIONS#######
          if session>=5:
               print("high freqency training")
          elif  session>=3 and session<=4:
             print("regular training")
     else:
              session<=3
              print("low freqeny training")
              if fitness_level== "advanced" and session>=5:
                  print(" higher advanced freqency training")
              ########FOR LOOP#######
              for i in (1,session +4):
                   print(f"workout sessions{4}")
                   
              

            

         

                     
          
     
      

               
             


               


     
       
     
        
    

