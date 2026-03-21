def binConvert(n: int) -> str:
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        remainder = n%2
        result = str(remainder) + result
        n = n//2
    return result

def intConverter(b: str) -> int:
    result = 0
    power = 0
    index = len(b) - 1
    while index >= 0:
        num = int(b[index]) * (2 ** power)
        result += num
        index -= 1
        power += 1
    return result



if __name__  == "__main__":
    print(binConvert(10))  # Output: "1010"
    print(binConvert(0))   # Output: "0"
    print(binConvert(255)) # Output: "11111111"
    print(intConverter("1010"))  # Output: 10
    print(intConverter("0"))     # Output: 0
    print(intConverter("11111111")) # Output: 255