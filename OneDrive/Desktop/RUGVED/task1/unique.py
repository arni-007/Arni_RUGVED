word=input("enter the word:")
string=str(word)

for i in sorted(set(string)):
    print(i,":", string.count(i))

nstring=str(sorted(set(string)))

print(nstring)