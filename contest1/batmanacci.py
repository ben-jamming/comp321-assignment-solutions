rawinput = input().split()
N = int(rawinput[0])
K = int(rawinput[1])
def batmanacci(N, K):
    if N == 1:
        return "N"
    if N == 2:
        return "A"
    lengths = [0] * (N+1)
    lengths[1], lengths[2] = 1, 1
    for i in range(3, N+1):
        lengths[i] = lengths[i-2] + lengths[i-1]
    while N > 2:
        if K <= lengths[N-2]:
            N -= 2
        else:
            K -= lengths[N-2]
            N -= 1
    
    return "N" if N == 1 else "A"

print(batmanacci(N,K))
