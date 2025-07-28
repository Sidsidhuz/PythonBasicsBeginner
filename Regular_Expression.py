import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
123a456b789
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
pat
mat
bat
'''
# sentence = 'Start a sentence and then bring it to an end happy'
# # ^       - Beginning of a String
# # $       - End of a String
# pattern = re.compile(r'[^b]at') # here '.' represents any character whether it is alphabets or special charater or anything
# matches = pattern.finditer(text_to_search)
#
#
# for match in matches:
#      print(match)
###################################################################################
# Quantifiers:
# *- 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3} - Exact
# Number
# {3, 4} - Range
# of
# Numbers(Minimum, Maximum)

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # {number} the number denote how many \d are the instead of writing '\d\d\d'
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#      print(match)
##############################################################################
# to match these
# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T

# pattern = re.compile(r'M[rs]s?\.?\s\w*')# '\.' a \ is added so that only . can be sorted # the '?' is used to check the occurrence of Mr followed by a '.' or without '.'
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
########################################################################
#match gmails
# emails = '''
# miketyson@gmail.com
# henry.cavill@university.edu
# jason-321-statham@my-work.net
# '''
# # pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')# '\.' a \ is added so that only . can be sorted # the '?' is used to check the occurrence of Mr followed by a '.' or without '.'
# pattern = re.compile(r'[\w+.-]+[\w+.]+@[\w+.-]+(com|edu|net)')
# matches = pattern.finditer(emails)
# for match in matches:
#     print(match)
###########################################################################
urls = '''
https://www.google.com
http://isro.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'[\w+]://\w*\.*\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)