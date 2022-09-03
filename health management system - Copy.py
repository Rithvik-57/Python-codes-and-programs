def getdate() :
 import datetime
 return datetime.datetime.now()

print("who are you ? Light ? Lelouch ? Eren ?")
def log():
 print("who are you ? Light ? Lelouch ? Eren ?")
n=input() #n=name
if n=="Light" :
 print("Log food or workout , Light ?")
 fwli=input() # fwli = food or workout of light
 if fwli=="food" :
      f=open("Light's diet.txt" , 'a')
      lfw=input("type the food items to log\n") # lf = light's food
      f.write (str([str(getdate())]) + "  " + lfw + "\n")
      print("logged")
      f.close()

 
 fwli=input("log food or workout ?") # fwli = food or workout of light
 if fwli=="workout" :
     f=open("Light's everyday workout.txt" , 'a')
     lfw=input("Type the workouts performed") #lw=light's workout
     f.write(str([str(getdate())]) + "  " + lfw + "\n") 
     print("logged")
     f.close()
