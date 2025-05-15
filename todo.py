import json
import os

file="tasks.json"
if not os.path.exists(file):
     with open(file,"w")as f:
          json.dump([],f)

def add(FileName,value):      #adds to a txt file
     with open(FileName,"r")as f:
          jsonstring=json.load(f)
     newTask={
          "Name":value,
          "mark":False,
          
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
                all+=task["Name"]+mark +"\n"
                mark=""
     return all
            
     

def mark_completed(fileName,value):#marks task as completed
    with open(fileName,"r") as f:
          temp=json.load(f)
    for task in temp:
          if(task["Name"]==value):
               task["mark"]=True
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
    
         
             


#main part
               
print("choose:\n",
      "1.Add task\n",
      "2.Delete task\n",
      "3.Mark task as complete\n",
      "4.view all task\n",)
uinput=int(input())
if(uinput==1):
    taskw=str(input("enter task to add: "))
    add(file,taskw)
    print("Task added")
elif(uinput==2):
     print("choose which one to delete:")
     print(allDataStr(file))
     print("")
     delete=input("write: ")
     deletion(file,delete)

elif(uinput==3):    
     print("choose which one is completed:")
     print(allDataStr(file))
     print("")
     completed=input("write: ")
     mark_completed(file,completed)         
elif(uinput==4):
      print("Tasks:")
      print(allDataStr(file))
else:
     print("wrong input")
