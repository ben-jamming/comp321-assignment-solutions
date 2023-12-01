
end_token = '$'

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class SuffixTree:

    def __init__(self):
        self.root = SuffixTreeNode()

    def insert(self,s):
        # Check if s is prefix of any other string before inserting
        curr = self.root
        for i,c in enumerate(s):
            if c in curr.children:
                curr = curr.children[c]

                if curr.is_end:
                    return True
            
            else:
                curr.children[c] = SuffixTreeNode()
                curr = curr.children[c]
            
            if i == len(s) - 1:
                curr.is_end = True

                if curr.children:
                    return True
                
            elif curr.is_end:
                return True
            
            return False

# def tests():
#     """
#     1 =< n =< 10,000 # number of phone #'s
#     1 =< t =< 40 # number of test cases
#     0 =< d =< 9, range for a phone #'s digits
#     """



def main():
    n = int(input())
    results = []
    for _ in range(n):
        numbers = int(input())
        t = SuffixTree()
        f = False
        for i in range(numbers):
            f = t.insert(input())
            if f:
                break
        results.append(f)
    for r in results:
        print("NO") if r else print("YES")

main()
    

                