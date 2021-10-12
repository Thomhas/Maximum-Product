
def getProduct(lst):
    first = lst[0]
    second = lst[1]
    third = lst[2]
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
    product = first * second * third
    return product





