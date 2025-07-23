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
'''
sentence = 'Start a sentence and then bring it to an end happy'
# ^       - Beginning of a String
# $       - End of a String
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d') # here '.' represents any character whether it is alphabets or special charater or anything
matches = pattern.finditer(text_to_search)


for match in matches:
    print(match)
