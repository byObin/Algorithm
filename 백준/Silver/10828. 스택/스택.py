from collections import deque
import sys

def push(x):
# push X: 정수 X를 스택에 넣는 연산이다.
    s.append(x)

def pop():
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(s) == 0:
        print('-1')
    else:
        print(s.pop())

def size():
# size: 스택에 들어있는 정수의 개수를 출력한다.
    print(len(s))

def empty():
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    if len(s) == 0:
        print(1)
    else:
        print(0)
    
def top():
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(s) == 0:
        print(-1)
    else:
        print(s[-1])

s = []

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
    elif command[0] == 'top':
        top()
    else:
        print('wrong command')
