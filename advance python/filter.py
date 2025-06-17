'''def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    '''
a = [1, 3, 5, 3434, 335, 45, 56, 35, 234, 54666, 2, 45, 56, 1, 23, 3, 8, 6]

new = list(filter(lambda x: x> 9, a))
print(new)