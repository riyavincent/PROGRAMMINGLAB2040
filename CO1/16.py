word=input("enter a string:")
first=word[0:len(word)//2]
second=word[len(word)//2:]
print(second[0]+first[1:],first[0]+second[1:])