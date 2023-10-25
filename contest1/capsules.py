R,C = list(map(int,input().split()))
rows = [list(map(lambda x: x if x== "-" else int(x),input().split())) for _ in range(R)]
N_Regions = int(input())
regions = []
for i in range(N_Regions):
    line = list(map(int,input().split()))
    N = line[0]
    line = [tuple(map(int,cell.split())) for cell in line[1:]]

    for section in line



