def game_is_winnable(stack1: int, stack2: int, table: dict) -> bool:
    if (stack1, stack2) in table:
        return table[(stack1, stack2)]

    if stack1 == 0 or stack2 == 0:
        table[(stack1, stack2)] = False
        return False

    smaller_stack = min(stack1, stack2)
    larger_stack = max(stack1, stack2)

    # Optimization: If removing blocks still leaves the current stack as the larger one
    # and this state has been explored, skip it
    for i in range(1, larger_stack // smaller_stack + 1):
        blocks_to_move = i * smaller_stack
        if blocks_to_move > larger_stack:
            break

        new_stack1 = stack1 - blocks_to_move if stack1 >= stack2 else stack1
        new_stack2 = stack2 - blocks_to_move if stack2 >= stack1 else stack2

        # Check if this state has been explored
        if (new_stack1, new_stack2) in table:
            continue

        if not game_is_winnable(new_stack1, new_stack2, table):
            table[(stack1, stack2)] = True
            return True

    table[(stack1, stack2)] = False
    return False

    

def main():
    stack1, stack2 = list(map(int,input().split()))
    table = {}
    result = game_is_winnable(stack1,stack2,table)

    if result:
        print("win")

    else:
        print("lose")        

def test():
    """Performs unit tests for game_is_winnable."""
    table = {}
    print(game_is_winnable(10**18, 11, table)) # Fails on this

test()