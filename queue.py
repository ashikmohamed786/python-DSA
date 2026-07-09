queue=[]
size=5

def enqueue(value):
    if len(queue) == size:
        print("queue is full")
    else:
        queue.append(value)
def dequeue():
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue.pop(0))
def front():
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue[0])
def rear():
    if len(queue)==0:
        print("queue is empty")
    else:
        print(queue[-1])
def insert_front(value):
    if len(queue)==size:
        print("queue is full")
    else:
        queue.insert(0,value)
def insert_middle(value):
    if len(queue)==size:
        print("queue is full")
    else:
        mid=len(queue)//2
        queue.insert(mid,value)
def is_empty():
    print(len(queue)==0)
def is_full():
    print(len(queue)==size)

enqueue(10)
enqueue(20)
enqueue(30)

front()
rear()
insert_front(5)
print(queue)
insert_middle(15)
print(queue)