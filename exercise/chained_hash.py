# 체인법으로 해시 함수 구현

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node: # 개별 버킷
    """해시를 구성하는 노드"""
    
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next    # 뒤쪽 노드 참조


class ChainedHash:
    """체인법으로 해시 클래스 구성""" 

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블 크기 지정
        self.table = [None] * self.capacity     # 해시 테이블 리스트로 선언

    def hash_value(self, key:Any) -> int:
        """key에 대응하는 해시값 구함"""
        if isinstance(key, int):    # key가 int형인 경우
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)    # key가 int형이 아닌 경우
    

    def search(self, key:Any) -> Any:
        """key인 원소 검색해 값 반환"""
        hash = self.hash_value(key)     # 검색하는 key의 해시값
        p = self.table[hash]            # 노드 주목(point)

        while p is not None:
            if p.key == key:
                return p.value  # 검색 성공
            p = p.next      # 뒤쪽 노드 주목

        return None         # 검색 실패
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key, 값이 value인 원소 추가"""
        hash = self.hash_value(key)     # 추가하는 key의 해시값
        p = self.table[hash]            # 노드 주목(point)

        while p is not None:
            if p.key == key:
                return False            # 추가 실패
            p = p.next                  # 뒤쪽 노드 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp         # 노드 추가
        return True                     # 추가 성공
    

    def remove(self, key: Any) -> bool:
        """키가 key인 원소 삭제"""
        hash = self.hash_value(key)     # 삭제할 key의 해시값
        p = self.table[hash]            # 노드를 주목
        pp = None                       # 바로 앞의 노드 주목

        while p is not None:
            if p.key == key:            # key 발견 시 아래 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True             # key 삭제 성공
            pp = p
            p = p.next                  # 뒤쪽 노드 주목
        return False                    # 삭제 실패(key 존재 x)
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()