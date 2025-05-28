import json
import os
import time

def clear_terminal(): # for cross platform
    os.system('cls' if os.name == 'nt' else 'clear')

file="tasks.json"
if not os.path.exists(file):
     with open(file,"w")as f:
          json.dump([],f)

class Task:
     def __init__(self,FileName):
          self.FileName=FileName
          pass
     def add(self,value):      #adds to a txt file
          current_time = time.strftime("%Y-%m-%d %I:%M %p",time.localtime())
          with open(self.FileName,"r")as f:
               jsonstring=json.load(f)
               if(len(jsonstring)==0):
                    index=1
               else:
                    index=jsonstring[-1]["Index"]+1
          
          newTask={
               "Index":index,
               "Name":value,
               "mark":False,
               "time_added":current_time,
               "time_completed": None
          
          }
          jsonstring.append(newTask)
          with open(self.FileName,"w")as f:
               json.dump(jsonstring,f,indent=4)
          
        
     def allDataStr(self):     #show's all data of a txt file
          with open(self.FileName,"r")as f:
               allRead=json.load(f)
               mark=""
               all=""
               for task in allRead:
                    if task["mark"]==True:
                         mark="(completed)"
                    if(task["time_completed"]==None):
                         all+=str(task["Index"])+" "+task["Name"]+mark +"      add time:"+task["time_added"]+"\n"
                         mark=""
                    else:
                         all+=str(task["Index"])+" "+task["Name"]+mark +"      add time:"+task["time_added"]+"      completion time:"+task["time_completed"]+"\n"
                         mark=""
          return all
               
          

     def mark_completed(self,value):#marks task as completed
          current_time = time.strftime("%Y-%m-%d %I:%M %p",time.localtime())
          with open(self.FileName,"r") as f:
               temp=json.load(f)
          for task in temp:
               if(task["Index"]==int(value)):
                    task["mark"]=True
                    task["time_completed"]=current_time
                    break
          with open(self.FileName,"w") as f:
               json.dump(temp,f,indent=4)
               print("Marked")
     def deletion(self,value):
          updated=[]
          with open(self.FileName,"r") as f:
               temp=json.load(f)
          for task in temp:
               if task["Index"]!=int(value):
                     updated.append(task)
               if(task["Index"]>int(value)):
                    task["Index"]-=1
          with open(self.FileName,"w") as f:
               json.dump(updated,f,indent=4)
               print("deleted")
    
         
             
task = Task(file)
exit=True
#main part
while(exit):              
     print("choose:\n",
          "1.Add task\n",
          "2.Delete task\n",
          "3.Mark task as complete\n",
          "4.view all task\n",
          "5.exit")
     try:
         uinput=int(input())
     except ValueError:
          print("wrong input\n enter a value between 1-5")
          time.sleep(1.5)
          clear_terminal()
          continue

     if(uinput==1):
          taskw=str(input("enter task to add: "))
          task.add(taskw)
          print("Task added")
          time.sleep(1.5) 
          clear_terminal()
     elif(uinput==2):
          print("choose which one to delete:")
          print(task.allDataStr())
          print("")
          delete=input("write: ")
          task.deletion(delete)
          time.sleep(1.5)
          clear_terminal()

     elif(uinput==3):    
          print("choose which one is completed:")
          print(task.allDataStr())
          print("")
          completed=input("write: ")
          task.mark_completed(completed)   
          time.sleep(1.5) 
          clear_terminal()  
     elif(uinput==4):
          print("Tasks:")
          print(task.allDataStr())
     elif(uinput==5):
          exit=False
          print("exiting..",end="")
          time.sleep(1)
          print(".",end="")
          time.sleep(1)
          print(".")
          time.sleep(1)
          clear_terminal()
