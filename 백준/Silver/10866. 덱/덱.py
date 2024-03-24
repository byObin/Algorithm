from collections import deque
import sys

def push_front(x):
# push_front X: 정수 X를 덱의 앞에 넣는다.
    dq.appendleft(x)

def push_back(x):
# push_back X: 정수 X를 덱의 뒤에 넣는다.
    dq.append(x)

def pop_front():
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다    
    if len(dq) == 0:
        print('-1')
    else:
        print(dq.popleft())

def pop_back():
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(dq) == 0:
        print('-1')
    else:
        print(dq.pop())

def size():
# size: 덱에 들어있는 정수의 개수를 출력한다.
    print(len(dq))

def empty():
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    if len(dq) == 0:
        print(1)
    else:
        print(0)
    
def front():
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(dq) == 0:
        print(-1)
    else:
        print(dq[0])

def back():
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(dq) == 0:
        print(-1)
    else:
        print(dq[-1])



dq = deque()

command_line = sys.stdin.readlines()[1:]

for i in command_line:
    command = i.split()
    
    if command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'pop_front':
        pop_front()
    elif command[0] == 'pop_back':
        pop_back()
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
