if __name__ == '__main__':
    a = arr = []
    b = []
    
    n = int(input().split())
    
    for _ in range(n):
        arr.append(map(int, input().strip().split()))
    print(arr)

    result = diagonalDifference(arr)

    print(result)

def diagonalDifference(arr):
    sum1 = sum2 = 0
    
    for i in range(n):
        for j in range(n):
            if (i == j):
                a.append(arr[i][j])
                
    print(a)
                
    i = j = 0
    for i in range(n):
        for j in range(n):
            if ((i + j) == (n - 1)):
                b.append(arr[i][j])
    print(b)
    
    i = j = 0
    for i in range(n):
        sum1 += a[i]
        
    print(sum1)
        
    for j in range(n):
        sum2 += b[j]
    print(sum2)
        
    dif = sum1 - sum2
    
    return abs(dif)
