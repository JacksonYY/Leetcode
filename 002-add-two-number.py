
# Time O(max(m,n)) Assume that m and n represents the length of l1 and l2 respectively
# Space O(max(m,n))

# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    add the two numbers and return it as a linked list
    '''
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype ListNode
        """
        result_head = ListNode(0)
        cur1 = l1
        cur2 = l2
        # store the head of result_list
        cur, tmp = result_head, 0

        while cur1 or cur2:
            val = tmp
            if cur1:
                val += cur1.val
                cur1 = cur1.next
            if cur2:
                val += cur2.val
                cur2 = cur2.next
            val, tmp = val % 10, val / 10
            cur.next = ListNode(val)
            cur = cur.next

        if tmp == 1:
            cur.next = ListNode(1)
        return result_head.next


if __name__ == '__main__':
    #a, a.next, a.next.next = ListNode(2), ListNode(5), ListNode(8)
    #b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    a = ListNode(0)
    b = ListNode(1)
    result = Solution().addTwoNumbers(a, b)
    while result:
        print result.val
        result = result.next

