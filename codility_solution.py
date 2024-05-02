def solution(R, V):
    initial_balance_A = 0
    initial_balance_B = 0
    
    # If there's only one transfer and it's 'B'
    if R == 'B':
        initial_balance_B = V[0]
        return [initial_balance_B, 0]
    
    # If transfers start with 'B'
    if R[0] == 'B':
        initial_balance_B = V[0]
        for i in range(1, len(R)):
            if R[i] == 'A':
                initial_balance_A = V[i]
                break
            initial_balance_B += V[i]
        return [initial_balance_B, initial_balance_A]
    # If transfers start with 'A'
    else:
        for i in range(len(R)):
            if R[i] == 'B':
                initial_balance_B = V[i]
                break
            initial_balance_A += V[i]
        initial_balance_B += initial_balance_A
        return [0, initial_balance_B]
    
    
# Test cases
print(solution("BAABA", [2, 4, 1, 1, 2]))  # Output: [2, 4]
print(solution("ABAB", [10, 5, 10, 15]))   # Output: [0, 15]
print(solution("B", [100]))                 # Output: [100, 0]