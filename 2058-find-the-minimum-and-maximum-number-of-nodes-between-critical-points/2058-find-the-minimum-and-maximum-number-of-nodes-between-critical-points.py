class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_crit(a, b, c):
            return (b.val - a.val) * (b.val - c.val) > 0
        crt = [0, 0]
        Min, idx = inf, 1
        prev, curr, nxt = head, head.next, head.next.next        
        while nxt:
            if is_crit(prev, curr, nxt):
                if crt[0]:
                    Min = min(Min, idx - crt[crt[1] > 0])
                crt[crt[0] > 0] = idx
            prev, curr, nxt = curr, nxt, nxt.next
            idx += 1
        if not crt[1]:
            return [-1, -1]
        return [Min, crt[1] - crt[0]]
