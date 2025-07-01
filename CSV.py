import csv

# CSV (Comma Seperated Values)

# Reading from a CSV file
# with open(r'G:\Pythoneering\Exptlab1\WorkOutExpt\dataone.csv','r' ) as csvfile, open('datatwo.csv','w') as csvfile2:
#     csv_reader = csv.reader(csvfile)
#     N = csv.writer(csvfile2)
#     for row in csv_reader:
#         N.writerow(row)
with open ('G:\Pythoneering\Exptlab1\WorkOutExpt\dataone.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    ls = [i for i in csvreader]
    with open('data3.csv','w',newline='') as csvw:
        csvwriter = csv.writer(csvw)
        csvwriter.writerows(ls)



# data = [['Name','Age','City'],
#         ['Alice', 25, 'New York'],
#         ['Bob',30,'Los Angeles']]
# with open('datatwo.csv','w') as newfile:
#     csv_writer = csv.writer(newfile)
#     csv_writer.writerows(data)

# with open('G:\Pythoneering\Exptlab1\WorkOutExpt\dataone.csv','r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for i in csv_reader:
#         print(i)
#
# with open('G:\Pythoneering\Exptlab1\WorkOutExpt\dataone.csv','r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     with open('data4.csv','w') as newfile:
#
#         fieldname = ['fname','lname','email']
#         csv_writer = csv.DictWriter(newfile,fieldnames=fieldname)
#         csv_writer.writeheader()
#         for i in csv_reader:
#             csv_writer.writerow(i)

import requests
val = requests.get('https://www.google.com')
print(val.text)
with open('g.html','w',newline='') as html:
    html.write(val.text)