#program to extract domain from a mail id
s = input("Enter an email id :")

if '@' in s and s.count('@') == 1 and " " not in s:
    k = s.split('@')
    k.pop(0)
    print(f"Domain :{k[0]}")
else:
    print("Domain not exist")
