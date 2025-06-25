import os


# check whether the provided that exists or not
print(os.path.exists('NewEnd.jpg')) # >>> Returns True if the path exists

# Make a new Directory
os.mkdir('NewDir')

# Remove a directory
os.rmdir('NewDir')

# Remove a file
os.remove('NewEnd.jpg')

# creating a file using the logic
newFile = 'NewEnd.jpg'
if os.path.exists(newFile):
    print('The file already exists!')
else:
    with open('G:\Pythoneering\Exptlab1\WorkOutExpt\maxresdefault.jpg','rb')as f,open(newFile, 'wb') as new:
        new.write(f.read())
        print("New file created")
