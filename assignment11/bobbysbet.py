import math

def good_bet(r,s,x,y,w) -> bool:
    p = s-r+1
    p_x = (math.comb(y,x) + p**x + (1-p)**(y-x)) * w
    return p_x >= 1
    

def main():
    n = int(input())
    results = [good_bet(*list(map(int,input().split())))  for _ in range(n)]

    for r in results:
        if r:
            print("yes")

        else:
            print("no")


main()