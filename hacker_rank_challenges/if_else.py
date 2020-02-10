def wierd(num):
    if num % 2 == 1 or 6 <= num <= 20:
        print('Weird')
    else:
        print('Not Weird')


wierd(int(input()))