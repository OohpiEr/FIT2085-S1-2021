def reverse_integer(n: int) -> int:
    result = 0
    while n > 0:
        result = (result*10)+(n%10)
        n //= 10
    return result

print(reverse_integer(2941))