
def getProduct(lst):

    #Organize the first three number manually to ensure that it works with negative numbers.

    first = lst[0]
    if lst[1] > first:
        second = first
        first = lst[1]

    else:
        second = lst[1]

    if lst[2] > second:
        if lst[2] > first:
            third = second
            second = first
            first = lst[2]
        else:
            third = second
            second = lst[2]
    else:
        third = lst[2]

    if (len(lst) > 3):
        for i in range(3, len(lst)):
            #check if integer is over the "threshold";

            if lst[i] > third:
                if lst[i] > first:
                    third = second
                    second = first
                    first = lst[i]
                elif lst[i] > second:
                    third = second
                    second = lst[i]
                else:
                    third = lst[i]

    product = first * second * third
    return product





