from random import randint
from time import time

urn_a=set()
urn_b=set()

#n=int(input("How many numbers to start with:"))

def count_state(n):
    for i in range(1,n+1):
        urn_a.add(i)

    # print("\nUrn A contains: {}".format(urn_a))
    # if len(urn_b)==0:
    #     print("Urn B contains: {}")

    num=randint(1,n+1)
    for i in range(num):
        x=randint(1,n+1)
        if x in urn_a:
            urn_a.remove(x)
            urn_b.add(x)

    #print("\nInitialization State\nUrn A contains: {}\nUrn B contains: {}".format(urn_a,urn_b))

    #print("\nSize of urn A: {}\nSize of urn B: {}".format(len(urn_a),len(urn_b)))

    steps=0
    while len(urn_b)!=0:
        x=randint(1,n+1)

        if x in urn_a:
            urn_a.remove(x)
            urn_b.add(x)
            steps+=1
        elif x in urn_b:
            urn_b.remove(x)
            urn_a.add(x)
            steps+=1
    
    return steps

    # print("\nEnd State\nUrn A contains: {}\nUrn B contains: {}".format(urn_a,urn_b))
    # print("Number of steps taken: {}".format(steps))

print("Balls\tSteps\tTime (ms)\n---------------------")
for i in range(2,25):
    t1=time()
    s=count_state(i)
    t2=time()-t1
    print("{}\t{}\t{:.3f}".format(i,s,t2*1000))