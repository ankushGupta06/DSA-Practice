#GCD (Greatest Common Divisor) and HCF (Heighest Common Factor) are the same thing

def loop(a,b):
    if (a == 0) and (b == 0):
        return max(a,b)

    result = max(a,b)

    while result > 0:
        if (a % result) == 0 and (b%result) == 0:
            break
        result -= 1
    return result

def euclideanSubtraction(a,b):
    if a == 0:
        return b
    if b == 0:
        return b
    if a == b:
        return a
    if a > b:
        return euclideanSubtraction(a-b,b)
    else:
        return euclideanSubtraction(a,b-a)
    
def euclideanRemainder(a,b):
    return a if b == 0 else euclideanRemainder(b,a%b)

if __name__ == "__main__":
    a,b = map(int,input().split())
    print(loop(a,b))