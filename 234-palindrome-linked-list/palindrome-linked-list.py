class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global front
        front = head
        def helper(back) -> bool:
            global front
            if not back:
                return True
            equal_so_far = helper(back.next)
            value_equal = (front.val == back.val)
            front = front.next
            return equal_so_far and value_equal
        
        return helper(head)