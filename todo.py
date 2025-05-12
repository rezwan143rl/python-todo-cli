
print("choose:\n",
      "1.Add task\n",
      "2.Mark task as complete\n",
      "3.view all task\n")
uinput=int(input())
if(uinput==1):
    taskw=str(input("enter task to add: "))
    with open("tasks.txt","a")as f:
        f.write(taskw)
elif(uinput==2):
     with open("tasks.txt","r")as f:
          allRead=f.read()
          print("choose which one is completed:")
          print(allRead) 
          completed=input("")
     with open("tasks.txt","r")as f:
          data1=[]
          data=True
          while data:
               data=f.readline()
               data=data.removesuffix("\n")
               data1.append(data)
          for el in range(len(data1)-1):
               if data1[el] == completed and "(completed)" not in data1[el]:
                    data1[el]+="(completed)" 
                       
     with open("tasks.txt","r+")as f:
           f.truncate(0)
           f.write('\n'.join(data1))

       
          
elif(uinput==3):
      with open("tasks.txt","r")as f:
          allRead=f.read()
          print("Tasks:")
          print(allRead) 
else:
     print("wrong input")

        


