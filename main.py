s1 = input("Введите любые числа через пробел: ")

s2 = [int(i) for i in s1.split()]

n = int(input("Введите любое целое число: "))
s2.append(n)
print("Исходный список: ", s2)


def sort(s2):
    for i in range(len(s2)):
        index_min = i
        for l in range(i, len(s2)):
            if s2[l] < s2[index_min]:
                index_min = l
        if i != index_min:
            s2[i], s2[index_min] = s2[index_min], s2[i]
    return s2


print("Итоговый список после сортировки:", sort(s2))
