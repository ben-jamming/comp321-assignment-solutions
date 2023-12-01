

def find_equal_sums(n, test_cases):
    results = []
    for case in test_cases:
        S = list(map(int, case.split()))
        n = len(S)
        table = {}
        found = False
        print(f"Processing case: {case}")  # Debugging print statement

        for i in range(1, (1 << n)):
            curr_sum = 0
            curr_subset = []

            for j in range(n):
                if (i & (1 << j)) != 0:
                    curr_subset.append(S[j])
                    curr_sum += S[j]

            print(f"Current subset: {curr_subset}, Current sum: {curr_sum}")  # Debugging print statement

            if curr_sum in table:
                print(f"Found two subsets with equal sum! {curr_subset} and {table[curr_sum]}")
                print(f"Their respective sums are {sum(curr_subset)} and {sum(table[curr_sum])}")  # Debugging print statement
                set1 = set(curr_subset)
                set2 = set(table[curr_sum])
                if set1 != set2:
                    results.append((" ".join(map(str, table[curr_sum])), " ".join(map(str, curr_subset))))
                    found = True
                    print("Found equal sum subsets!")  # Debugging print statement
                    break
            else:
                table[curr_sum] = curr_subset.copy()

        if not found:
            results.append("Impossible")
            print("No equal sum subsets found for this case.")  # Debugging print statement

    return results
    
n = int(input())
test_cases = [input() for _ in range(n)]
results = find_equal_sums(n,test_cases)
for r in range(len(results)):
    print(f"Case #{r+1}:")
    if results[r] == "Impossible":
        print(results[r])
    else:
        print(results[r][0])
        print(results[r][1])
