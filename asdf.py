# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None



# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)


# a = head
# b = head


# temp = head
# while temp:
#     print(temp.data, end=" -> " if temp.next else "")
#     temp = temp.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next





# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0

#             total = x + y + carry
#             carry = total // 10

#             current.next = ListNode(total % 10)
#             current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy.next



# def create_list(arr):
#     dummy = ListNode()
#     current = dummy
#     for num in arr:
#         current.next = ListNode(num)
#         current = current.next
#     return dummy.next



# def print_list(head):
#     while head:
#         print(head.val, end=" -> " if head.next else "")
#         head = head.next
#     print()



# l1 = create_list([2, 4, 3])  
# l2 = create_list([5, 6, 4])  # Represents 465

# solution = Solution()
# result = solution.addTwoNumbers(l1, l2)

# print("Result:")
# print_list(result)
    