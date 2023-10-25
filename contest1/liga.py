def fix_formatting(team):
    return [int(x) if x != '?' else x for x in team]

def fill_missing_fields(teams_data):
    # Define the functions to calculate missing values
    def calc_T(W, D, L):
        return W + D + L

    def calc_P(W, D):
        return 3 * W + D

    def calc_W(P, D):
        return (P - D) // 3

    def calc_D(P, W):
        return P - 3 * W

    def calc_L(T, W, D):
        return T - W - D

    # Resultant list
    filled_data = []

    # Process each team's data
    for data in teams_data:
        T, W, D, L, P = data

        # First pass: Fill using direct relationships
        if W != '?' and D != '?':
            P = calc_P(W, D)
        if P != '?' and D != '?':
            W = calc_W(P, D)
        if P != '?' and W != '?':
            D = calc_D(P, W)
        if W != '?' and D != '?' and L != '?':
            T = calc_T(W, D, L)
        if T != '?' and W != '?' and D != '?':
            L = calc_L(T, W, D)

        # Second pass: Fill using secondary relationships
        if T != '?' and W != '?' and D != '?':
            L = calc_L(T, W, D)
        if T != '?' and W != '?' and L != '?':
            D = T - W - L
        if T != '?' and D != '?' and L != '?':
            W = T - D - L

        filled_data.append([T, W, D, L, P])

    return filled_data


n = int(input())
standings = []
teams = [standings.append(fix_formatting(input().split())) for _ in range(n)]
filled_standings = fill_missing_fields(standings)
for team in filled_standings:
    print(' '.join([str(x) for x in team]))


