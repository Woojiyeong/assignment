def div_name(full_name: str):
    name_parts = full_name.strip().split()
    
    if len(name_parts) >= 2:
        last_name = name_parts[0]
        first_name = " ".join(name_parts[1:])
    else:
        last_name = name_parts[0]
        first_name = ""
    
    return last_name, first_name

name = input("이름:")
last, first = div_name(name)
print("성:", last)
print("이름:", first)