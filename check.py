

def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    print(nums)
    count = 0
    for ele in ar:
        print(ar,',',k)
        print(f'{ele} ele')
        modu = ele % k
        print(f'{modu} modu')
        
        count += nums[(k - modu) % k]
        print(f'{ (k - modu) % k} (k - modu) % k')
        print(f'{count} count')
        nums[modu] += 1
        print(f'{nums[modu]} nums[modu]')
        print(f'{nums} nums')

        print('---------------------------')
    return count



n =4
k = 5
ar = [2,4,8,18]
print(divisibleSumPairs(n,k,ar))