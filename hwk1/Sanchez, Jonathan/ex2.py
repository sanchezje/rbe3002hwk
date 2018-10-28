

def ispalindrome(arr):

    length = len(arr)
    if length == 0:
        return True
    if length == 1:
        return True

    x = arr.pop(0)
    y = arr.pop(len(arr)-1)

    if x == y:
        return ispalindrome(arr)
    else:
        return False

