

def tenth_base(number, base: int):
    number = str(number)
    solution = 0
    current_power = len(number) - 1
    
    for i in number:
        solution += int(i) * (base ** current_power)
        current_power -= 1
    
    return solution

