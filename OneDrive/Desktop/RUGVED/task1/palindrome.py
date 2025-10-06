n=(input("enter the number:"))
l=len(n)

flag=0
for i in range (0,l):
    if n[i]==n[l-1-i]:
        flag=0
    else:
        flag=1
        break

if flag==0:
    print("it's a palindrome")

else:
    print("not a palindrome")

m=reversed(n) 
print(m)
if n==m:
    print("palindrome")
else:
    print("not a palindrome")