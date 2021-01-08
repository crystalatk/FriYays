# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
# candies = [2,3,5,1,3]
# extraCandies = 3
# Expected output: [true, true, true, false, true]


def most_candies(hit_list, extra):
    boo_list = []
    for i in hit_list:
        add_extra = i + extra
        boo_item = False
        for j in hit_list:
            if add_extra >= max(hit_list):
                boo_item = True
        boo_list.append(boo_item)
    return boo_list


candies = [2, 3, 5, 1, 3]
extraCandies = 3

print(most_candies(candies, extraCandies))

new_candies = [11, 23, 22, 10, 21]
extraCandies2 = 3

print(most_candies(new_candies, extraCandies2))
