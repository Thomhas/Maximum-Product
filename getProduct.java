
def getProduct(lst):
    first = 0
    second = 0
    third = 0
    for i in range(len(lst)):
        if lst[i] > first:
            third = second
            second = first
            first = lst[i]
        elif lst[i] > second:
            third = second
            second = lst[i]
        elif lst[i] > third:
            third = lst[i]
    return first*second*third





