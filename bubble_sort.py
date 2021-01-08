def bubble_sort(list_1):
    for j in range(len(list_1)-1):
        for i in range(len(list_1)-1):
            if list_1[i] > list_1[i+1]:
                a = list_1[i]
                b = list_1[i+1]
                list_1[i] = b
                list_1[i+1] = a

    return list_1


print(bubble_sort([2, 4, 6, 3, 11, 5, 1]))

print(bubble_sort([3, 1, 4, 2]))


# def bubble(list_2):
#     sorted = False
#     while not sorted:
#         for i in range(len(list_2)-1):
#             sorted = True
#             if list_2[i] > list_2[i+1]:
#                 list_2[i], list_2[i+1] = list_2[i+1], list_2[i]
#                 sorted = False
#     return list_2


# print(bubble([2, 4, 6, 3, 11, 5, 1]))

# print(bubble([3, 1, 4, 2]))
