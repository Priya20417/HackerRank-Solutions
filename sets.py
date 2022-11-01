def average(array):
    sets=set(array)
    k=sum(sets)
    res=k/len(sets)
    return res
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
