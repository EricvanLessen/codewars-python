def create_phone_number(n):
    area_code = ''.join(map(str, n[:3]))
    first_part = ''.join(map(str, n[3:6]))
    second_part = ''.join(map(str, n[6:]))
    
    formatted_number = f"({area_code}) {first_part}-{second_part}"
    return formatted_number

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
