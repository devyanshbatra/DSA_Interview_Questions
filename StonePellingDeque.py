from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    dq = deque(map(int, input().split()))
    turn = 1  # Aman: 1, Akshat: 0.
    lastPlayer = -1
    while len(dq) > 1:
        if turn == 1:
            # Aman’s turn: rotate then discard.
            top = dq.popleft()
            dq.append(top)
            if len(dq) == 1:
                lastPlayer = 1
                break
            dq.popleft()  # Discard.
            lastPlayer = 1
        else:
            # Akshat’s turn: rotate twice then discard.
            top = dq.popleft()
            dq.append(top)
            if len(dq) == 1:
                lastPlayer = 0
                break
            top = dq.popleft()
            dq.append(top)
            if len(dq) == 1:
                lastPlayer = 0
                break
            dq.popleft()  # Discard.
            lastPlayer = 0
        turn = 1 - turn  # Alternate turns.
    
    print(lastPlayer, dq[0])