from queue import PriorityQueue
q = PriorityQueue()
q.put((1, 'work'))
q.put((-1, 'life'))
q.put((1, 'drink'))
q.put((-2, 'sleep'))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get(block=False))
print(q.get())

# 数字越小，优先级越高，越先被取出来


# 如果可选参数 block 是 true 并且 timeout 是 None。默认阻塞，无穷等待。
# 若 block 为 False，不等待直接抛出空异常。
