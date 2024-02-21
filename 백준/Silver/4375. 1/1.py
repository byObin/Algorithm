while True:
    try:
        n = int(input())
    except:
        break

    ones = 1
    i=1
    
    while True:
        if ones % n == 0:
            print(i)
            break

        ones += 10**i
        i+=1