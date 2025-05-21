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
     newTask={
          "Name":value,
          "mark":False,
          "time_added":current_time,
          "time_completed":""
          
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
                if(task["time_completed"]==""):
                    all+=task["Name"]+mark +"      add time:"+task["time_added"]+"\n"
                    mark=""
                else:
                     all+=task["Name"]+mark +"      add time:"+task["time_added"]+"      completion time:"+task["time_completed"]+"\n"
                     mark=""
     return all
            
     

def mark_completed(fileName,value):#marks task as completed
    current_time = time.strftime("%Y-%m-%d %I:%M %p",time.localtime())
    with open(fileName,"r") as f:
          temp=json.load(f)
    for task in temp:
          if(task["Name"]==value):
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
         if task["Name"]!=value:
              updated.append(task)
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
     uinput=int(input())
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
     else:
          print("wrong input")
