result = []

def handling(result):
    inp = input().split()
    command = inp[0]
    values = inp[1:]
    if command == 'print':
        print(result)
    else:
        execute = 'result.' + command + "(" + ",".join(values) + ")"
        eval(execute)

for num in range(int(input())):
    handling(result)