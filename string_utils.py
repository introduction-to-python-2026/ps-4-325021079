def split_before_each_uppercases(formula):
    new_list = []
    start = 0
    for i in range(len(formula)):     
        char = formula[i]   
        if i > 0 and char.isupper():       
            new_list.append(formula[start:i])     
            start = i      
    if start < len(formula):
        new_list.append(formula[start:])     
    return new_list






def split_at_first_digit(formula) :
    split_list = []
    
    for i in formula[1:] :
          if i.isdigit():
              split_list = (formula[0:formula.index(i)] , int(formula[formula.index(i):]) )
              break
    if len(split_list) == 0:
      split_list = (formula , 1)
    return split_list

