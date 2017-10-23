for i in range(101):
    if (i%6) == 0:
        ans = 'Fizzbuzz'
    elif (i%2) == 0:
        ans = 'Fizz'
    elif (i%3) ==0:
        ans = 'Buzz'
    else:
        ans = '___'
    print '%d: %s' % (i, ans)

