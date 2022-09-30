for i in range(1,26):

    out = ""

    if i % 3 == 0: out += 'Fizz'
    if i % 5 == 0: out += 'Buzz'
    
    print(i, out)