
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

print(prefix)
for i in range(n-1, 0, -1):
    suffix[i] = max(suffix[i+1], nums[i])
print(suffix)
for i in range(len(queries)):
    max_value = max(prefix[queries[i][0]], suffix[queries[i][1]])
    print(max_value)
