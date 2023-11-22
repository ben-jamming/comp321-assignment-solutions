import math

def good_bet(r,s,x,y,w) -> bool:
    p = (s-r+1)/s
    p_x = 0
    for i in range(x,y+1):
        p_x += math.comb(y,i)* (p**i) * ((1-p)**(y-i))
    return p_x * w > 1
    

def main():
    n = int(input())
    results = [good_bet(*list(map(int,input().split())))  for _ in range(n)]

    for r in results:
        if r:
            print("yes")

        else:
            print("no")


main()