class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size=0
        curr=head
        while curr:
            size+=1
            curr=curr.next
        mid=(size)//2
        curr=head
        for i in range(mid):
            curr=curr.next
        return curr        
        