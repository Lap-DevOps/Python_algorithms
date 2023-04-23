import collections


q = collections.deque()
q.append(1)
q.append(2)
q.pop()
q.appendleft(0)
q.popleft()
print(q)