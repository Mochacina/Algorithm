S, P = map(int, input().split())
DNA = input()
dna = ['A', 'C', 'G', 'T']
dna_cnt = [0]*4
dna_chk = [*map(int, input().split())]

def insert(n):
    for i in range(len(dna)):
        if dna[i] == n:
            dna_cnt[i] += 1

def delete(n):
    for i in range(len(dna)):
        if dna[i] == n:
            dna_cnt[i] -= 1
            
def check():
    for i in range(len(dna)):
        if dna_cnt[i] < dna_chk[i]:
            return False
    return True

for i in DNA[:P]: insert(i)

ans = 1 if check() else 0


for i in range(P, S):
    insert(DNA[i])
    delete(DNA[i-P])
    if check():
        ans += 1
        
print(ans)

# change code to use dictionary