import timeit


def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))


t1 = timeit.timeit(stmt=doIt, number=10)
print(t1)