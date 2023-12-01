# def find_destination(start_pole, rungs):
#     current_pole = start_pole
#     # Traverse down the rungs
#     for rung in rungs:
#         if rung[0] == current_pole:
#             current_pole = rung[1]  # Move right
#         elif rung[1] == current_pole:
#             current_pole = rung[0]  # Move left
#     return current_pole

def ghost_leg(n, rungs):
    prm = list(range(1, n + 1))
    for rung in rungs:
        a = rung - 1 
        prm[a], prm[a + 1] = prm[a + 1], prm[a]
        
    return prm

n, m = map(int, input().split())
rungs = [int(input()) for _ in range(m)]
for r in ghost_leg(n, rungs):
    print(r)
