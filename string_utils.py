def spdef split_before_each_uppercases(formula):
  new_list = []
  start = 0
  end = 0
  for i in formula:
    if i.isupper():
      start = formula.index(i)

      for e in formula[start]:
        if e.isupper:
          end = formula.index(e)
          new_list.append(formula[start:end])
          formula[:end+1]

  return new_list


def split_at_first_digit(formula) :
    split_list = []
    
    for i in formula[1:] :
          if i.isdigit():
              split_list = [formula[0:formula.index(i)] , int(formula[formula.index(i):]) ] 
              break
    if len(split_list) == 0:
      split_list = [formula , 1]
    return split_list

