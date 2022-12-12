import sys 

sys.stdin = open("킹.txt")

move = {
    "R": (0,1),
    "L": (0,-1),
    "B": (1,0),
    "T": (-1,0),
    "RT":(-1,1),
    "LT":(-1,-1),
    "RB":(1,1),
    "LB":(1,-1)
}

K, S, N = input().split()

# 좌표 구하기 x,y 
# A1 --> A,1 
K_y = 8 - int(K[1])
K_x = ord(K[0])-65

S_y = 8 - int(S[1])
S_x = ord(S[0])-65

for _ in range(int(N)):
    delta = input()

    ky = K_y + move[delta][0]
    kx = K_x + move[delta][1]

    if 0 <= ky < 8 and 0 <= kx < 8 and ky == S_y and kx == S_x:
        sy = S_y + move[delta][0]
        sx = S_x + move[delta][1]
        if 0 <= sy < 8 and 0 <= sx < 8:
            K_y = ky
            K_x = kx 
            S_y = sy 
            S_x = sx
    elif 0 <= ky < 8 and 0<= kx < 8:
        K_y = ky 
        K_x = kx 



print(f'{chr(K_x+65)}{8-K_y}')
print(f'{chr(S_x+65)}{8-S_y}')
