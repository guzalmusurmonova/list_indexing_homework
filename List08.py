def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    n=0 
    while n<len(list1):
        if list1[n]==1:
            list1[n]=True 
        if list1[n]==0:
            list1[n]=False 
        n=n+1
    return list1 
print(main( [1, 0, 1, 1, 0]))