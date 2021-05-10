def bubble_sort(lst, desc=False):
    moves = 0 # stop parameter
    while not moves: #if there were no changes in lst stop
        moves = 1 #stop parametr
        for i in range(0, len(lst) - 1):
            if float(lst[i]) > float(lst[i+1]): # if a[i] > a [i+1]
                lst[i], lst[i+1] = lst[i+1], lst[i] #chang a[i] and a[i+1]
                moves = 0 #stop parametr if there was change

    if desc: # to reverse if asked
        lst = lst[::-1]
    return lst

'''
в любом случае делаю сортировку по возрастанию
параметр moves означает были ли замены на цикле (изначально в теле цикла =1, при необходимости замены 2 элементов местами параметр = 0)
если замен не было (параметр = 1), то в таком случае новый "круг" не нужен, сортировка закончена
если desc=true, то переворачиваем отсортированный список
'''
