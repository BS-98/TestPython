def check_numbers(number):        
    number   = str(number)
    num_prev = 0
    nb       = 0
    digits   = []
    rep      = False
    
    for num in number:
        if int(num) < int(num_prev):
            rep = True
            break
            
        if num == num_prev:
            digits.append(num)
            nb += 1
    
        num_prev = num
        
    if nb >= 2 and len(set(digits)) >= 2 and rep == False:
        return True

    else:
        return False 




nums = [] #list to see these numbers
for num in range(372**2, 809**2 + 1):
    check = check_numbers(num)
    
    if check == True:
        nums.append(num)
    
print("Numbers which meet all three criteria:", len(nums))
