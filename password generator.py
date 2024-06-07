import random
n=int(input("Enter number of digits for the password"))
l1=[]
list1=[1,2,3,4,5,6,7,8,9,0]
for i in range(n):
        if i%2==0:
            a= int(random.choice(list1))
            l1.append(a)
        elif i%3==0:
            for i in (97,123):
                l1.append(chr(i))
                break
        elif i%5==0:
            for i in (65,90):
                l1.append(chr(i))
                break
        else:
            for i in range(58,64,1):
                l1.append(chr(i))
                break
l2=[]        
for e in l1:
     l2.append(str(e))
s=""
print(s.join(l2))