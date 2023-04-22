def solve(s: str) -> int:
    s = s.replace(" ", "")
    s = s.split("+")
    list2 = []
    total_sum = 0
    for element in range(len(s)):
        total_multiply = 1
        if s[element].isdigit():
            total_sum += int(s[element])
        else:
            list2 += s[element].split("*")
            while list2:
                total_multiply *= int(list2.pop())
            total_sum += total_multiply
    return total_sum


while True:
    print(solve(input("Ingrese la cuenta a resolver: ")))
