from collections import deque
import sys

def push(x):
# push X: 정수 X를 큐에 넣는 연산이다.
    q.append(x)

def pop():
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(q) == 0:
        print('-1')
    else:
        print(q.popleft())

def size():
# size: 큐에 들어있는 정수의 개수를 출력한다.
    print(len(q))

def empty():
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    if len(q) == 0:
        print(1)
    else:
        print(0)
    
def front():
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(q) == 0:
        print(-1)
    else:
        print(q[0])

def back():
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(q) == 0:
        print(-1)
    else:
        print(q[-1])


q = deque()
command_line = sys.stdin.readlines()[1:]

for i in command_line:
    command = i.split()
    
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
    else:
        print('wrong command')
