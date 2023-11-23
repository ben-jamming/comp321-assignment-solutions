line = int(input())
numbers = []
while line != 0:
    numbers.append("{ "+ ", ".join([str(3**(j)) for j,i in enumerate(bin(line-1)[2:][::-1]) if i == "1"])+" }")
    line = int(input())
for r in numbers:
    print(r)