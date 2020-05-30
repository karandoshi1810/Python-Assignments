# -*- coding: utf-8 -*-
"""Practice-22-5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k6b3LXNi2DyxAodtfDqdsJgavtnbqSy8
"""

'''
Task-1.1:
*
**
***
****
'''
for i in range(0,5):
  print("*"*i)
print("\n")

'''
Task 1.2:
1
23
345
4567
'''
for i in range(1,5):
  sum = i
  for j in range(1,i+1):
    print(sum,end="")
    sum = sum + 1
  print("")
print("\n")

'''
Task-1.3:
1234
123
12
1
'''
for i in range(1,5):
  for j in range(1,6-i):
    print(j,end=(""))
  print("")
print("\n")

'''
Task-1.4:
ENGG
ENG
EN
E
'''
string = 'ENGG'
length = len(string)
for i in range(0,len(string)+1):
  print(string[0:length-i:1])
  

'''
Task-1.5:
    4
   34
  234
 1234
'''
for i in range(0,4):
  sum = 4-i
  for j in range(3-i):
    print(" ",end = (""))
  for k in range(0,i+1):
    print(sum,end=(""))
    sum=sum+1
  print("\n")
  
'''
Task 1.6:
      1
     121
    12321
   1234321
'''
for i in range(1,5):
  for j in range(0,5-i):
    print(" ",end="")
  for k in range(1,i+1):
    print(k,end="")
  for l in range(i-1,0,-1):
    print(l,end = "")
  print("")

  #All programs complied and ran successully

#Task-2.1:ake two range as an Input.Find which range have max Prime Numbers

#Taking ranges
range1 = int(input("Enter range 1:"))
range2 = int(input("Enter range 2:"))
#counters for both ranges
range1count=0
range2count=0
i=j=0
#flags for both ranges
flag1=0
flag2=0
for i in range(2,range1+1): #this for loop will move till the entered value, i.e if 14 is enterd it will check till 14. We will not check for 1. As 1 is neither prime nor composite
  flag1=0                   #flag indicator = 0 
  for j in range(2,int(i//2)+1): #this loop will check whether or not the number from upper loop is divided by any other number in the given range
    if(i%j==0):             #if yes then it is not prime number and will indicate it by making flag1=1 and we will move to next number for checking
      flag1=1
      break
  if(flag1==0):             #we will check if the flag == 0 then i is a prime number because it is not divided by any other value in range and will add 1 to its counter

    range1count+=1
i=j=0
for i in range(2,range2+1):  #this for loop will move till the entered value, i.e if 14 is enterd it will check till 14. We will not check for 1. As 1 is neither prime nor composite
  flag2=0                    #flag indicator = 0 
  for j in range(2,int(i//2)+1): #this loop will check whether or not the number from upper loop is divided by any other number in the given range
    if(i%j==0):              #if yes then it is not prime number and will indicate it by making flag1=1 and we will move to next number for checking
      flag2=1
      break
  if flag2==0:               #we will check if the flag == 0 then i is a prime number because it is not divided by any other value in range and will add 1 to its counter
    range2count+=1
print("Total numbers of prime numbers in range 1 is:",range1count)
print("Total numbers of prime numbers in range 2 is:",range2count)
if range1count>range2count:  #we will check which range has greater number of prime numbers based on their counters
  print("Range 1 has greater number of prime numbers\n")
elif range2count>range1count:
  print("Range 2 has greater number of prime numbers\n")


#Task2.2:Find all Perfect Number from 2 to N.[e.g. 28 = 1+2+4+7+14 ]
prange = int(input("Enter your range:"))
sum=0
count=0
for i in range(2,prange+1):
  sum=0
  for j in range(1,i):
    if i%j==0:
      sum+=j
  if(sum==i):
    print(sum,end=("\n"))
    count+=1
print(f"Total number of perfect numbers are:{count}\n")


#Task2.3:Find first 20 Palindrome Number starts from 10
num=100
count=0
temp = 0
rem = 0
print("Palindrome numbers are:",end = "\n")
while count<20:
  temp = num
  rev_num=rem=0

  while temp>0:
    rem = int(temp)%10
    rev_num = int(rev_num*10) + rem
    temp = int(temp)//10
  if int(rev_num) == int(num):
    count = int(count)+1
    print(rev_num,end=("\t"))
  num+=1
  

#All programs complied and ran successully

#Task3:How many records are stored in file? Print all record from last to first on screen

#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
input_file.close()
i=0
total_records = 0
file1 = open("Input.txt","r")
file2 = open("Output.txt","w")

data = file1.read()
data_rev=''
data_first = ''
for rec in data.split("\n"):
  if i==0:
    data_first = rec
    i = i + 1
  else:
    data_rev = rec+"\n"+data_rev
    total_records += 1
data_rev = data_first + data_rev
file2.write(data_rev)
print("Total number of records are:",total_records-1,file = file2)
file1.close()
file2.close()

#This program complied and ran successully

#Task-4:Print first and last record on output screen.

#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
file1 = open("Input.txt","r")
data = file1.read()
count=0
for record in data.split("\n"):
  count+=1
  if count == 1:
    print(record)
  elif count == 7:
    print(record)

file1.close()

#This program complied and ran successully

#Task-5:Which student having more ATKT? Print his/her name

#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
file1 = open("Input.txt","r")
file2 = open("Output.txt","w")
fail_sub_3 = 0
fail_sub_4 = 0
for rec in range(0,5):
  data = file1.readline()
  if rec==3:
    x = data.split(",")
    for i in range(1,4):
      if int(x[i])<=40:
        fail_sub_3 +=1

  elif rec==4:
    x = data.split(",")
    for i in range(1,4):
      if int(x[i]) <= 40:
        fail_sub_4 +=1
  else:
    continue

if fail_sub_3 > fail_sub_4:
  file2.write("Yuvraj Singh")
elif fail_sub_4 > fail_sub_3:
  file2.write("MS Dhoni")

file1.close()
file2.close()

#This program complied and ran successully

#Task - 6:Which student get maximum marks in Subject-2?Print that student’s name on screen

'''
#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
input_file.close()
'''
i=0
max_sub_2=0
name = ''
indicator = 0
file1 = open("Input.txt","r")

for i in range(0,8):
  data = file1.readline()
  if indicator == 0:
    indicator+=1
    continue
  x = data.split(",")
  if int(x[2])>int(max_sub_2):
    max_sub_2 = int(x[2])
    name = x[0]
print(name)


file1.close()

#This program complied and ran successully

#Task-7:Which subject’s result is having maximum marks?
'''
#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
input_file.close()
'''
file1 = open("Input.txt","r")
file2 = open("Output.txt","w")
indicator = 0
result_sub1=0
result_sub2=0
result_sub3=0
maximum_result=0
for i in range(0,8):
  data = file1.readline()
  if indicator == 0:
    indicator = indicator + 1
    continue

  else:
    x = data.split(",")
    result_sub1 = int(result_sub1) + int(x[1])
    result_sub2 = int(result_sub2) + int(x[2])
    result_sub3 = int(result_sub3) + int(x[3])
if result_sub1>result_sub2:
  if result_sub1>result_sub3:
    maximum_result = 1
  else:
    maximum_result = 2
elif result_sub2>result_sub3:
  maximum_result = 2
else:
    maximum_result = 3 
print("Maximum result is of subject:",maximum_result)

file2.write("Maximum result is of subject:")
file2.write(str(maximum_result))
file1.close()
file2.close()
#this program compiled and ran successfylly

#Task - 8 Prepare Result for Notice Board:
#Sr No | Name | Sub1 | Sub2 | Sub3 | Total | Result

'''
#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
input_file.close()
'''
file1 = open("Input.txt","r")
file2 = open("Output.txt","w")
indicator = 0
total = 0
result = 0
s_no=0
for i in range(0,8):
  result = 0
  total = 0
  data = file1.readline()
  if indicator == 0:
    file2.write("Sr No | Name | Sub1 | Sub2 | Sub3 | Total | Result\n")
    indicator += 1
    continue

  else:
    s_no+=1
    x = data.split(",")
    for i in range(1,4):
      total = int(total) + int(x[i])
    result = abs((int(total)/300)*100)
    file2.write(str(s_no)+"|"+str(data.rstrip())+"|"+str(total)+"|"+str(result)+"\n")

file1.close()
file2.close()

#This program complied and ran successully

#Task-9:Who get consistent marks in all subjects?


#opening file Input in "w" mode
input_file = open("Input.txt","w")
input_file.write("Student Name , Sub1 , Sub2 , Sub3\n"
                  "Virat Kohli, 70, 56, 45\n"
                  "Suresh Raina, 80,28, 39\n"
                  "Yuvraj Singh, 69, 40,25\n"
                  "MS Dhoni,12, 15,17\n"
                  "Rohit Sharma,97,90,79\n"
                  "Shikhar Dhawan,66, 90,90\n"
                  "Rahul Dravid, 40, 58, 59\n"
)
input_file.close()

file1 = open("Input.txt","r")
file2 = open("Output.txt","w")
indicator = 0
minimum = 0
name = ""

for i in range(0,8):
  total = 0
  average = 0
  result = 0
  data = file1.readline()
  if indicator == 0:
    indicator += 1
    continue
  else:
    x = data.split(",")
    for j in range(1,4):
      total = int(total) + int(x[j])
    average = int(total)/3

    for k in range(1,4):
      result = int(result) + abs(int(average)-int(x[k]))
    if indicator==1:
      minimum = result
      indicator += 1
    else:
      if int(result)<int(minimum):
        minimum = result
        print(minimum,sep=("\t") )
        name = x[0]
print(name)
print("Student with minimum marks is:",name,file = file2)

file1.close()
file2.close()

#This program complied and ran successully

