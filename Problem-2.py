'''
    Time Complexity: O(nlogk)
    Space Complexity: O(k)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = None
        index = 0

        if not lists:
            return result

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, index, head))
                index += 1

        while len(heap):
            nodeTuple = heapq.heappop(heap)
            nodeval = nodeTuple[0]
            node = nodeTuple[2]
            
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
                index += 1

            newNode = ListNode(nodeval)

            if not result:
                result = newNode
                prev = newNode
            else:
                prev.next = newNode
                prev = newNode

        return result
            