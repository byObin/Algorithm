from __future__ import annotations
from typing import Any, Type

class Node:
    """연결리스트용 노드 클래스"""
    def __init__(self, data: Any = None, next: Node = None):
        """초기화(Node = data + next)"""
        self.data = data
        self.next = next    # 뒤쪽 노드에 대한 참조 포인터

class LinkedList:
    """연결 리스트 클래스"""
    def __init__(self) -> None:
        self.no = 0         # 노드의 개수
        self.head = None    # head node
        self.current = None # current node

    def __len__(self) -> int:
        """연결 리스트의 노드 개수 반환"""
        return self.no
    
    def search(self, data: Any) -> int:
        """data와 값이 같은 노드 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data 포함 여부 확인"""
        return self.search(data) >= 0
    
    def add_first(self, data: Any) -> None:
        """맨 앞에 노드 삽입"""
        ptr = self.head # 삽입 전의 head node
        self.head = self.current = Node(data, ptr)  # 삽입할 node 생성, head가 삽입한 노드 참조하도록 update
        self.no += 1
        
    def add_last(self, data: Any):
        """맨 끝에 노드 삽입"""
        if self.head is None:   # 리스트 비어있는 경우
            self.add_first(data)    # 맨 앞에 노드 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next      
            ptr.next = self.current = Node(data, None) # 삽입할 node 생성, ptr.next가 새로 삽입한 node 참조하도록 update
            self.no += 1

    def remove_first(self) -> None:
        """head node 삭제"""
        if self.head is not None:   # 리스트가 비어있지 않다면
            self.head = self.current = self.head.next   # 삭제하기 전 head node가 참조했던 node 참조

    def remove_last(self):
        """ 꼬리 node 삭제 """
        if self.head is not None:
            if self.head.next is None:  # 노드가 1개라면
                self.remove_first()     # head node 삭제
            else:
                ptr = self.head     # 스캔 중인 node
                pre = self.head     # 스캐 중인 node의 앞쪽 node

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None     # pre는 삭제 뒤 꼬리 노드
                self.current = pre
                self.no -= 1
    def remove(self, p: Node) -> None:
        """노드 p 삭제"""
        if self.head is not None:
            if p is self.head:      # p가 head node면
                self.remove_first() # head node 삭제
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return      # ptr이 리스트에 존재 x
                    
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
    
    def remove_current_node(self) -> None:
        """ 주목 노드 삭제 """
        self.remove(self.current)

    def clear(self) -> None:
        """전체 노드 삭제"""
        while self.head is not None:       # 전체가 비어 있을 때까지
            self.remove_first()             # head node 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """주목 노드 한칸 뒤로 이동"""
        if self.current is None or self.current.next is None:
            return False    # 이동 불가능
        self.current = self.current.next
        return True
    
    def print_current_node(self) -> None:
        """주목 노드 출력"""
        if self.current is None:
            print("no ptr node")
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드 출력"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        """이터레이터 반환"""
        return LinkedListIterator(self.head)
        

class LinkedListIterator:
    def __init__(self, head: None):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data