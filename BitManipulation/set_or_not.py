def is_set(n: int, pos: int) -> bool:
    return (n>>pos) & 1 == 1

def set_bit(n: int, pos: int) -> int:
    return n | (1<<pos)

def clear_bit(n: int, pos: int) -> int:
    return n & ~(1<<pos)

def toggle_bit(n: int, pos: int) -> int:
    return n ^ (1<<pos)

def count_set_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def count_clear_bits(n: int) -> int:
    total_bits = n.bit_length()
    set_bits = count_set_bits(n)
    return total_bits - set_bits 

def remove_last_set_bit(n: int) -> int:
    return n & (n - 1)

def remove_last_clear_bit(n: int) -> int:
    return n | (n + 1)

def bitwise_operations(a: int, b: int) -> dict:
    return {
        'AND': a & b,
        'OR': a | b,
        'XOR': a ^ b,
        'NAND': ~(a & b),
        'NOR': ~(a | b),
        'XNOR': ~(a ^ b)
    }

if __name__ == "__main__":
    n = 29  # Binary: 11101
    pos = 2
    print(f"Is bit at position {pos} set in {n}? {is_set(n, pos)}")  # True
    print(f"Set bit at position {pos} in {n}: {set_bit(n, pos)}")    # 29
    print(f"Clear bit at position {pos} in {n}: {clear_bit(n, pos)}")# 25
    print(f"Toggle bit at position {pos} in {n}: {toggle_bit(n, pos)}")# 25
    print(f"Count of set bits in {n}: {count_set_bits(n)}")          # 4
    print(f"Count of clear bits in {n}: {count_clear_bits(n)}")      # 1
    a = 12  # Binary: 1100
    b = 10  # Binary: 1010
    ops = bitwise_operations(a, b)
    for op, result in ops.items():
        print(f"{op} of {a} and {b}: {result}")
