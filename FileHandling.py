# File Handling in python (Text)

# x - create a file
# r - read mode
# w - write mode (Overwrites the file)
# a - append mode (will not overwrite the file)
# b - binary mode ( used to access binary files)

#basic way to access a text file in python
file = open('1.txt','w+')
file.write("last line ")
print(file.read())

#write into txt file
with open('1.txt','w') as f:
    f.write('hello world - 1 \nBetween ')
    f.write('hello world - 2  \n ')


# Read from a txt file
with open('1.txt','r') as f:
     lines = f.readlines() #stores as a list ie; type(lines) -> list()
# print(lines)    # print(t)
s = 'sid'

# append +

with open('1.txt','r+') as f:
    lines = f.readlines()
    print(lines)


# seek operation - used to initialize file pointer

with open('1.txt','r') as f:
    # f.seek(0)
    l = f.read()
    print('seek')
    print(l)
    f.seek(0)

# peek operation - used to see the location of the file pointer


