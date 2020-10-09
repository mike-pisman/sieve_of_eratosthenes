def Bruteforce(n):
    def IsPrime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    for i in range(2, n + 1):
        if IsPrime(i):
            yield i

if __name__ == "__main__" :
    bruteforce(3000)