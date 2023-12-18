# Medium
# Uses heap/priority queue + greedy
# Passes all test cases
import heapq
class Solution:
    
    def reorganizeString(self, s: str) -> str:
        char_counts = {}
        for c in s:
            char_counts[c] = char_counts.get(c, 0) + 1

        heap = [(-count, char) for char, count in char_counts.items()]
        heapq.heapify(heap)

        prev_char, prev_count = None, 0
        new_s = []

        while heap:
            count, char = heapq.heappop(heap)
            new_s.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            prev_count, prev_char = count + 1, char 
        return ''.join(new_s) if len(new_s) == len(s) else ""

