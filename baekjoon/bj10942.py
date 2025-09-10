# Hmph! For this genius beautiful girl programmer, Lady Helena, it's absolutely a piece of cake!
# A million queries? Pfft. They should know a simple loop won't cut it.
# This calls for a more... elegant solution. Dynamic Programming, my dear!
import sys

# Faster I/O for my precious CPU time!
input = sys.stdin.readline

def solve():
    """
    Solves the BJ10942 Palindrome problem using Dynamic Programming.
    """
    try:
        n_str = input()
        if not n_str: return
        n = int(n_str)
        
        numbers = list(map(int, input().split()))
        
        m_str = input()
        if not m_str: return
        m = int(m_str)

    except (IOError, ValueError) as e:
        # Hehe, even my perfect code should handle pesky errors.
        # print(f"Debug: Input error - {e}")
        return

    # Let's build a truth table of palindromes. It's like creating a cheat sheet for the future!
    # dp[start][end] = 1 if numbers[start...end] is a palindrome.
    # Using 0-based indexing because it's the professional way.
    dp = [[0] * n for _ in range(n)]

    # 1. Base case: length 1.
    # Duh. Even a teddy bear knows any single number is a palindrome.
    for i in range(n):
        dp[i][i] = 1
        # print(f"Debug: dp[{i}][{i}] = 1 (length 1)")

    # 2. Base case: length 2.
    # Only if they're twinsies!
    for i in range(n - 1):
        if numbers[i] == numbers[i+1]:
            dp[i][i+1] = 1
            # print(f"Debug: dp[{i}][{i+1}] = 1 (length 2, numbers[{i}]==numbers[{i+1}])")

    # 3. Now for the real magic! For lengths 3 to n.
    # A long sequence is a palindrome if its ends match and the inside is *also* a palindrome.
    # It's like a Russian doll of palindromes!
    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            # print(f"Debug: Checking length {length}, start={start}, end={end}")
            if numbers[start] == numbers[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1
                # print(f"Debug: dp[{start}][{end}] = 1 (numbers match and inner part is palindrome)")

    # With my pre-calculated cheat sheet, I can answer any of their silly questions in a flash!
    # O(1) baby! Yes! I am the one and only Helena!
    results = []
    for _ in range(m):
        try:
            s, e = map(int, input().split())
            # Adjust to 0-based indexing for my perfect DP table.
            results.append(str(dp[s-1][e-1]))
        except (IOError, ValueError):
            continue
    
    print("\n".join(results))

solve()


# import sys
# input = sys.stdin.readline

# def solve():
#     try:
#         n_str = input()
#         if not n_str: return
#         n = int(n_str)
        
#         numbers = list(map(int, input().split()))
        
#         m_str = input()
#         if not m_str: return
#         m = int(m_str)

#     except (IOError, ValueError) as e:
#         return

#     dp = [[0] * n for _ in range(n)]

#     for i in range(n):
#         dp[i][i] = 1

#     for i in range(n - 1):
#         if numbers[i] == numbers[i+1]:
#             dp[i][i+1] = 1
            
#     for length in range(3, n + 1):
#         for start in range(n - length + 1):
#             end = start + length - 1
#             if numbers[start] == numbers[end] and dp[start+1][end-1] == 1:
#                 dp[start][end] = 1
                
#     results = []
#     for _ in range(m):
#         try:
#             s, e = map(int, input().split())
#             results.append(str(dp[s-1][e-1]))
#         except (IOError, ValueError):
#             continue
    
#     print("\n".join(results))

# solve()