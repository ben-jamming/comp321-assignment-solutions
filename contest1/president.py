from math import ceil

def minimum_voters_to_convince(S, state_data):
    total_delegates = sum(data[0] for data in state_data)
    total_constituent_delegates = 0
    needed_votes = []
    
    for D, C, F, U in state_data:
        if C > F + U:
            total_constituent_delegates += D
        elif F <= C + U:
            votes_needed = ceil((F + U - C + 1) / 2)
            efficiency = votes_needed / D
            needed_votes.append((efficiency, votes_needed, D))
            
    needed_votes.sort()
    total_votes_needed = 0
    
    for _, votes, delegates in needed_votes:
        total_constituent_delegates += delegates
        total_votes_needed += votes
        if total_constituent_delegates > total_delegates / 2:
            return total_votes_needed
        
    return "impossible"

def main():
    S = int(input().strip())
    states = [tuple(map(int, input().strip().split())) for _ in range(S)]
    print(minimum_voters_to_convince(S, states))

main()
