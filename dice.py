import random

def dice_list(pip, li):
    results = []             
    for _ in range(li):          
        results.append(random.randint(1, pip))
                             
    return results              

outcomes = dice_list(6, 3)     
print(outcomes)
