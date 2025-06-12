def rec(l):
    sum = 0
    for i in l:
        if type(i) == list:
            sum += rec(i)
        elif type(i) == int:
            sum += i
    return sum

ls = [1,2,[3,4],[5,6],5,[10]]
print(rec(ls))

#devin@gofreelab.com