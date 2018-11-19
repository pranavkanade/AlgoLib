def arrayManipulation(n, queries):
    arr = [0]*n
    for l in queries:
        i, j, inc = l
        arr[i-1] += inc
        if j < n: arr[j] -= inc
    temp = 0
    maxi = 0
    for el in arr:
        temp += el
        if(maxi < temp): maxi = temp
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()