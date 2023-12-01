
def firstnumber(improved):
    for char in improved:
        try:
            return str(int(char))
        except:
            continue

def lastnumber(improved):
    return firstnumber(improved[::-1])

with open('1/input','r') as values:
    sum = 0
    for value in values:
        sum += int(firstnumber(value)+ lastnumber(value))


print(sum)