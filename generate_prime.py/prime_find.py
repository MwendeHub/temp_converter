def prime_find(n):
    for i in range(1,n):
        prime = True
    for x in range(2,i):
        if i % x != 0:
            prime = False
    if True:
        print prime 