class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        previous_head_last_node = None
        answer = None
        
        while start:
            allow, node, new_head, previous_head_last_node, original_node, base_case_reached = self.recursiveReverseK(
                k, 1, start, previous_head_last_node, start
            )
            if base_case_reached or allow:
                node.next = None
            if answer is None:
                answer = original_node
            start = new_head
        return answer

    def recursiveReverseK(self, k, count, node, previous_head_last_node, original_head):
        if not node:
            if previous_head_last_node and original_head:
                previous_head_last_node.next = original_head
            return [False, node, None, None, None, True]
        
        if k == count:
            if previous_head_last_node:
                previous_head_last_node.next = node
            return [True, node, node.next, node, node, False]
        
        result = self.recursiveReverseK(k, count + 1, node.next, previous_head_last_node, original_head)
        if result[5]:
            node.next = None
        
        if result[0] and result[1]:
            result[1].next = node
            result[3] = node
        
        return [result[0], node, result[2], result[3], result[4], False]