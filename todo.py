import json
import os
import time

def clear_terminal(): # for cross platform
    os.system('cls' if os.name == 'nt' else 'clear')

file="tasks.json"
if not os.path.exists(file):
     with open(file,"w")as f:
          json.dump([],f)

def add(FileName,value):      #adds to a txt file
     current_time = time.strftime("%Y-%m-%d %I:%M %p",time.localtime())
     with open(FileName,"r")as f:
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
     with open(FileName,"w")as f:
          json.dump(jsonstring,f,indent=4)
          
        
def allDataStr(FileName):     #show's all data of a txt file
     with open(FileName,"r")as f:
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
            
     

def mark_completed(fileName,value):#marks task as completed
    current_time = time.strftime("%Y-%m-%d %I:%M %p",time.localtime())
    with open(fileName,"r") as f:
          temp=json.load(f)
    for task in temp:
          if(task["Index"]==int(value)):
               task["mark"]=True
               task["time_completed"]=current_time
               break
    with open(fileName,"w") as f:
         json.dump(temp,f,indent=4)
         print("Marked")
def deletion(fileName,value):
    updated=[]
    with open(fileName,"r") as f:
        temp=json.load(f)
    for task in temp:
         if task["Index"]!=int(value):
              updated.append(task)
              if(task["Index"]>int(value)):
                   task["Index"]-=1
    with open(fileName,"w") as f:
         json.dump(updated,f,indent=4)
         print("deleted")
    
         
             

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
          add(file,taskw)
          print("Task added")
          time.sleep(1.5) 
          clear_terminal()
     elif(uinput==2):
          print("choose which one to delete:")
          print(allDataStr(file))
          print("")
          delete=input("write: ")
          deletion(file,delete)
          time.sleep(1.5)
          clear_terminal()

     elif(uinput==3):    
          print("choose which one is completed:")
          print(allDataStr(file))
          print("")
          completed=input("write: ")
          mark_completed(file,completed)   
          time.sleep(1.5) 
          clear_terminal()  
     elif(uinput==4):
          print("Tasks:")
          print(allDataStr(file))
     elif(uinput==5):
          exit=False
          print("exiting..",end="")
          time.sleep(1)
          print(".",end="")
          time.sleep(1)
          print(".")
          time.sleep(1)
          clear_terminal()
