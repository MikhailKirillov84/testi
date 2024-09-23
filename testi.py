#for i in range(len('sum')):
#    if i != 2:
#        print('sum'[i], end='-')
#    else:
#        print("sum"[1])
#from proba.probnik import result

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem < 5:
        print(elem)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = [elem for elem in a if elem in b]#- #Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

print(result)


# Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = dict(sorted(d.items(), key=operator.itemgetter(1)))
result1 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print(result, result1)



