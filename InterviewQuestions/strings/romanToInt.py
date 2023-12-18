#Easy
# Passes all test cases
import re
class Solution:
    
    def romanToInt(self, s: str) -> int:
        sub_values = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC": "LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC"
        }
        num_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num_list = s.split()
        res = re.compile("|".join(sub_values.keys())).sub(lambda ele: \
            sub_values[re.escape(ele.group(0))], s)
        result = sum([num_to_int[x] for x in res])
        print(result)
        return result