file="tasks.txt"
def add(FileName,value):      #adds to a txt file
     with open(FileName,"a")as f:
        value="\n"+value
        f.write(value)
def allDataStr(FileName):     #show1s all data of a txt file
     with open(FileName,"r")as f:
          allRead=f.read()
          return allRead

def mark_completed(FileName,value): #marks task as completed
     temp=allDataStr(FileName)
     data=temp.split('\n')
     checker =value+"(completed)"
     for el in range(len(data)):
          if data[el] == value and "(completed)" not in data[el]:
               data[el]+="(completed)"
               break
          if data[el]==checker:
               print("Task was completed before")
               return              
     with open(file,"r+")as f:
           f.truncate(0)
           f.write('\n'.join(data))
           print("Marked as completed")
def deletion(fileName,value):
     temp=allDataStr(fileName)
     data=temp.split('\n')
     checker =value+"(completed)"
     for el in range(len(data)-1):
          if data[el] == value or data[el] == checker:
               data.pop(el)
     with open(file,"r+")as f:
           f.truncate(0)
           f.write('\n'.join(data))
           print("Deleted")
             


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

        


