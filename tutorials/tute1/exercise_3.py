def deci_to_hex(inp: int) -> str:
    hex_letters = ["A","B","C","D","E","F"]
    result = ""
    while inp != 0:
        rem = inp%16
        if rem > 9:
            rem = hex_letters[rem-10]
        else:
            rem = str(rem)
        result = rem + result
        inp = inp//16
    return result