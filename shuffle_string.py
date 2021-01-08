# Given a string s and an integer list indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# s = “odce”
# indices = [1, 2, 0, 3]
# Returns “code”

# def sort_list(list_1):
#     for j in range(len(list_1)-1):
#         for i in range(len(list_1)-1):
#             if list_1[i] > list_1[i+1]:
#                 a = list_1[i]
#                 b = list_1[i+1]
#                 list_1[i] = b
#                 list_1[i+1] = a
#     return list_1


def sort_string(list_2, code):
    new_string = ""
    for j in code:
        for i in range(0, len(list_2)):
            if i == code[j]:
                new_string += list_2[i]
    return new_string


s = "odce"
indices = [1, 2, 0, 3]

# print(s[indices[0]])

print(sort_string(s, indices))

# Carter solution
string = "odce"
indices = [1, 2, 0, 3]
word = []

i = 0
while i < len(string):
    word.append(string[i])
    i += 1

i = 0
finished = False
j = 0
while finished == False:
    if indices[i] > indices[i + 1]:
        indices[i], indices[i + 1] = indices[i + 1], indices[i]
        word[i], word[i + 1] = word[i + 1], word[i]
    else:
        j += 1
    i += 1
    if i == len(indices) - 1:
        i = 0
        if j == len(indices) - 1:
            finished = True
        else:
            j = 0

print(word)
