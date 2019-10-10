from random import randint

lst1=[]
n=int(input("How many numbers to start with: "))
lst1=[x for x in range(1,n+1)]

print("list 1 contains ",format(lst1))

lst2=[]
rand_num=randint(0,n)
print("Numbers to put in list 2 = ",format(rand_num))
for i in range(rand_num):
  x=randint(1,n+1)
  if x not in lst2 and x in lst1:
    lst2.append(x)
    lst1.remove(x)
  else:
    x=randint(1,n+1)


print("list 1 contains \n",lst1)
print("list 2 contains \n",lst2)

steps = 0
while(len(lst2)!=0):
  x=randint(1,n+1)
  if x in lst1 and x not in lst2:
    lst1.remove(x)
    lst2.append(x)
  elif x in lst2 and x not in lst1:
    lst2.remove(x)
    lst2.append(x)
  
  steps+=1

print("list 1 contains\n",lst1)
print("list 2 contains\n",lst2)
print("number of steps taken: ",steps)