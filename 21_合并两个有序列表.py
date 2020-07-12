# 21 合并两个有序列表
'''
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
# 递归思想！！时间、空间复杂度O(len(l1)+len(l2))
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  #设置终止条件 其中一条链表遍历完
        if not l2: return l1
        if l1.val<=l2.val:  # 将列表指向较小值的链表
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

# 迭代思想！！
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)  # 创建哑节点
        tmp=dummy  #临时链表 哑节点会跟着tmp走！！！！
        while l1 and l2:
            if l1.val<=l2.val:
                tmp.next=l1
                l1=l1.next
            else:
                tmp.next=l2
                l2=l2.next
            tmp=tmp.next
        tmp.next=l1 if l1 else l2
        return dummy.next