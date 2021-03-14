str=input("enter a string")
n=str[0];
result=str[1:].replace(n,'$')
print(n+result)