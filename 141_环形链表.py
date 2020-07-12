# 141 环形链表
'''
判断一个链表是否为环形链表
'''

# 暴力法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a=set()
        while head:
            if head.next in a:
                return True
            a.add(head.next) #储存链表
            head=head.next
        return False

# 快慢指针 若为环形链表，指针必相逢
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a=b=head
        while b and b.next: #保证快指针存在
            a=a.next
            b=b.next.next
            if a is b:
                return True
        return False

# 赋值法  将遍历过的节点打上标记 再次遍历时即为环形
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val=='zcy':
                return True
            head.val='zcy'
            head=head.next
        return False