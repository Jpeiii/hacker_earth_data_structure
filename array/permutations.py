'''
You are given a permutation with length n. You want to play a game with you friend, Bob, and the rule will be as follows: 

You will choose a subarray [l,r] from the permutation. Then, ask Bob to find the maximum element in the rest of the numbers.
You are given a permutation  contains all numbers 1 to n. And, in  queries, each query has two integers l and r .

For each query, you have to help Bob find the maximum value that does not exist in the subarray [l,r].

'''
n, q = map(int, input().split())
nums = list(map(int, input().split()))

queries = []

for _ in range(q):
    q = list(map(int, input().split()))
    queries.append(q)

prefix = [1 for i in range(n+2)]
suffix = [1 for i in range(n+2)]

for i in range(2, n+1):
    prefix[i] = max(prefix[i-1], nums[i-2])

for i in range(n-1, 0, -1):
    suffix[i] = max(suffix[i+1], nums[i])

for i in range(len(queries)):
    max_value = max(prefix[queries[i][0]], suffix[queries[i][1]])
    print(max_value)
