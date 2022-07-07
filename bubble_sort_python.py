def bubble_sort_python(ls: list)->list:
  for i in range(0,len(ls)):
    for j in range(i+1, len(ls)):
        if(ls[i]>ls[j]):
            m = ls[i]
            ls[i] = ls[j]
            ls[j] = m
  return ls
