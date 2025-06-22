# File Handling in python (Text)

#basic way to access a text file in python
file = open('1.txt','r')
print(file.read())

#write into txt file
with open('1.txt','w') as f:
    f.write('hello world - 1 \nBetween ')
    f.write('hello world - 2  \n ')


# Read from a txt file
with open('1.txt','r') as f:
     lines = f.readlines() #stores as a list ie; type(lines) -> list()
print(lines)    # print(t)