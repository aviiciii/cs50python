inpt = input('Expression: ').split()
x = float(inpt[0])
y = float(inpt[2])
opr = inpt[1]
if opr == '+':
    print(f"{x+y:.1f}")
elif opr == '-':
    print(f"{x-y:.1f}")
elif opr == '*':
    print(f"{x*y:.1f}")
elif opr == '/':
    print(f"{x/y:.1f}")