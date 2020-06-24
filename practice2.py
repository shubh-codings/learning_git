n,k = (int(x) for x in input().split())
lst = list(map(int, input().split()))

count = 0
for i in range(len(lst)-1):
    for x in range(1+i, len(lst)):     
        if (lst[i] + lst[x]) % k == 0:
            count += 1
        
print(count)




def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    count = 0
    for ele in ar:
        modu = ele % k
        count += nums[(k - modu) % k]
        nums[modu] += 1
    return count




def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    count = 0
    for ele in ar:
        modu = ele % k
        print(f"{ele} {modu} {count} {nums} - after modu")
        count += nums[(k - modu) % k]
        print(f"{ele} {modu} {count} {nums} - after count+=")
        nums[modu] += 1
        print(f"{ele} {modu} {count} {nums} - after nums+=")
        print("-----------------------")
    return count