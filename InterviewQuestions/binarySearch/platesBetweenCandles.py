# Medium
# Passes all test cases
# Note: This solutiion could definitely be faster
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        candles = []
        plates_count = [0] * n

        plate_counter = 0
        for i, char in enumerate(s):
            if char == '|':
                candles.append(i)
            else:  # char == '*'
                plate_counter += 1
            plates_count[i] = plate_counter

        def right_candle(index):
            left = 0
            right = len(candles) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if candles[mid] < index:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(candles) else None

        def left_candle(index):
            left = 0
            right = len(candles) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if candles[mid] <= index:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if right >= 0 else None

        answer = []
        for left, right in queries:
            left_candle_index = right_candle(left)
            right_candle_index = left_candle(right)

            if left_candle_index is not None and right_candle_index is not None and left_candle_index <= right_candle_index:
                plates = plates_count[candles[right_candle_index]] - plates_count[candles[left_candle_index]]
                answer.append(plates)
            else:
                answer.append(0)

        return answer
                