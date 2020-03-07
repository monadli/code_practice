def string_to_number (input_string):
    output = 0
    input_string = input_string.strip()
    neg = 0

    for i in range(0, len(input_string)):
        output *= 10
        current = ord(input_string[i])
        if(current == 45 and len(input_string) > 1 and i == 0):
            neg = 1
        elif(current > 47 and current < 58):
            output += current - 48
        else:
            return None
    
    if(neg):
        output *= -1
    
    return output
