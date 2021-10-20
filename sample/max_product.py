from typing import List
from functools import reduce


def max_product(lst: List[int]):

    highest: (int, int, int)  # holds highest numbers in the list
    lowest: (int, int, int) = (0, 0, 0)  # holds lowest numbers in the list
    negative_count: int = 0

    if len(lst) > 3:
        # Iterate through the list

        # Sets the 3 first numbers:
        if lst[1] > lst[0]:
            highest = (lst[1], lst[0])
        else:
            highest = (lst[0], lst[1])

        if lst[2] > lst[1]:
            if lst[2] > lst[0]:
                highest = (lst[2], highest[0], highest[1])
            else:
                highest = (highest[0], lst[2], highest[1])
        else:
            highest = (highest[0], highest[1], lst[2])

        # Iterates through the list
        for i in range(3, len(lst)):
            print(highest)
            if lst[i] < 0:
                negative_count += 1
            # checks for lowest integers
            # first checks if it is under the threshold (in this case the third lowest number)
            if lst[i] < lowest[2]:
                if lst[i] < lowest[0]:
                    lowest = (lst[i], lowest[0], lowest[1])
                elif lst[i] < lowest[1]:
                    lowest = (lowest[0], lst[i], lowest[1])
                else:
                    lowest = (lowest[0], lowest[1], lst[i])

            # checks for highest integers
            # first checks if it is over the threshold (in this case the third highest number)
            if lst[i] > highest[2]:
                if lst[i] > highest[0]:
                    highest = (lst[i], highest[0], highest[1])
                elif lst[i] > highest[1]:
                    highest = (highest[0], lst[i], highest[1])
                else:
                    highest = (highest[0], highest[1], lst[i])

        if negative_count == len(lst):
            # In case all numbers on the list are negative
            return reduce(lambda acc, num: acc*num, lowest)
        else:
            print(highest)
            positive_product: int = reduce(lambda acc, num: acc*num, highest)
            negative_product: int = lowest[0] * lowest[1] * highest[0]
            return max(positive_product, negative_product)

    # If the input list has 3 or less integers there is no need to go through it
    else:
        return reduce(lambda acc, num: acc*num, lst)
