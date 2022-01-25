def hello(arr,n):
    count=0
    for i in range(len(arr)-1):
        j=i+1
        arr_n=arr[j:]
        m=max(arr_n)
        if arr[i] > m:
            count+=1
    return (count+1)



n = int(input())
arr=list(map(int, input().split()))
print(hello(arr,n))