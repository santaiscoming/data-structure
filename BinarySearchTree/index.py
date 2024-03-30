from __future__ import annotations
from typing import Any, Type
from collections import deque


class Node:
    def __init__(self, key: Any, value: Any, left: Node, right: Node):
        # 노드 번호 : 이진트리에서는 key로 정렬되어있다
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        # 초기화
        self.root = None

    def search(self, key: Any):
        curr_node = self.root

        while True:
            if curr_node is None:
                return None
            if key == curr_node.key:
                return curr_node.value

            if key < curr_node.key:
                curr_node = curr_node.left
            elif key > curr_node.key:
                curr_node = curr_node.right

    def add(self, key, value) -> bool:
        def add_node(node: Node, key: Any, value: Any):

            if key == node.key:
                return False

            # case 1 : key가 주목 node보다 작음
            #   if key 왼쪽에 값이 있는가 ?
            #     없다 -> 왼쪽노드에 삽입
            #     있다 -> 왼쪽노드를 주목노드로
            #   else : key 오른쪽 동일하게 수행
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            # case 2 : key가 주목 node보다 큼
            #     오른쪽에 값이 있는가 ?
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)

            return True

        # 만약 root가 비어있으면 넣는다
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any):
        curr_node = self.root  # 스캔중인 노드
        # why get parent ? -> 스캔중인 삭제후 삭제한 노드의 자식노드를 연결해줘야함
        parent = None  # 스캔중인 노드 부모
        del_node_was_left_child = (
            False  # 삭제할 노드(스캔중인 노드)가 왼쪽노드였는지 오른쪽이었는지 알아야함
        )

        # 자식이 없는가
        #   -> 해당 노드 검색 후 삭제
        # 자식이 1개인가
        #   -> 해당 노드의 부모에 자식을 연결
        # 자식이 2개인가
        #   -> ???
        # ------------- 노드 검색  -------------
        while True:
            # 해당 노드가 없으면 더이상 진행 X
            if curr_node is None:
                return False

            if key == curr_node.key:
                break  # 찾았다 !
            else:
                # 가지치면서 내려가기전에 부모를 저장
                parent = curr_node
                # 이후에 부모의 자식을들 순회하며 자식들중에 찾고자하는 key node가 있는지 검사
                # 그리고 찾으면 curr_node에 key(find) node의 자식을 저장
                if curr_node.key < key:  # 왼쪽 탐색
                    del_node_was_left_child = True
                    curr_node = curr_node.left
                else:  # 오른쪽 탐색
                    del_node_was_left_child = False
                    curr_node = curr_node.right

        # ------------- 삭제할 노드의 자식의 자식이 한개 -------------
        # 현재 변수 현황
        # curr_node = 삭제하고자 하는 node
        # parent = curr_node (삭제하고자 하는 노드의 부모)
        # 1. 왼쪽이 없다
        if curr_node.left is None:
            # curr_node = 삭제할 노드 자식 (오른쪽)
            if curr_node == self.root:
                parent = curr_node.right
            elif curr_node.right is None:
                if del_node_was_left_child:
                    parent.left = curr_node.right
                else:
                    parent.right = curr_node.right

        elif curr_node.right is None:
            if parent is self.root:
                self.root = curr_node.left
            elif del_node_was_left_child:
                parent.left = curr_node.left
            else:
                parent.right = curr_node.left

        # ------------- 삭제할 노드의 자식의 자식이 두개 -------------
        else:
            parent = curr_node
            left = curr_node.left
            del_node_was_left_child = (
                True  # 왼쪽자식중에서 가장큰놈을 부모의 왼쪽에 붙여야하기때문
            )

            # left의 right가 없으면 left를 바로 붙임
            while left.right is not None:
                parent = left
                left = left.right
                del_node_was_left_child = False

            curr_node.key = left.key
            curr_node.value = left.value

            if del_node_was_left_child:
                parent.left = left.left
            else:
                parent.right = left.right

        return True

    def remove2(self, node: Node, key: Any):
        def _find_min_node(node):
            while node is not None and node.left is not None:
                node = node.left

            return node

        if node is None:
            return None

        # 내가 찾는 노드야
        if node.key == key:
            # case 1 : 자식 0개
            # case 2 : 자식 1개
            # case 3 : 자식 2개
            return
        # 내가 찾는 노드가 아니야 (근데 키가 작음)
        elif node.key > key:
            node.left = self.remove2(node.left, key)
        elif node.key < key:
            node.left = self.remove2(node.right, key)

        return node
        # 내가 찾는 노드가 아니야 (근데 키가 큼)

    def dump(self, reverse=False):
        def print_sub_tree(root):
            if root is None:
                return

            print_sub_tree(root.left)
            print("방문 ! ", root.key)
            print_sub_tree(root.right)

        def print_sub_tree_reverse(root):
            if root is None:
                return

            print_sub_tree_reverse(root.right)
            print("방문 ! ", root.value)
            print_sub_tree_reverse(root.left)

        if not reverse:
            print_sub_tree(self.root)
        else:
            print_sub_tree_reverse(self.root)

    def bfs(self):
        dq = deque()

        dq.appendleft(self.root)
        while len(dq) != 0:
            node = dq.popleft()
            print(node.key, "->", end="")
            if node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)

    def min_key(self):
        if self.root is None:
            raise Exception("root가 없습니다 !")

        node = self.root

        while node is not None and node.left is not None:
            node = node.left

        return node.key

    def max_key(self):
        if self.root is None:
            raise Exception("root가 없습니다 !")

        node = self.root

        while node is not None and node.right is not None:
            node = node.right

        return node.key


tree = BinarySearchTree()
tree.add(10, 1)
tree.add(7, 1)
tree.add(15, 999)
tree.add(4, 1)
tree.add(8, 1)
tree.add(9, 1)
tree.add(3, 1)
tree.add(5, 1)
tree.add(6, 1)

print(tree.root.key)
print("search node val : ", tree.search(15))
print("min key : ", tree.min_key())
print("max key : ", tree.max_key())
