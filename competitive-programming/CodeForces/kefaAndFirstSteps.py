input()
s = list(map(int, input().split()))
seq = 0
l = s[0]
m_seq = 0

for i in s:
    if i >= l:
        seq += 1
        l = i
    else:
        m_seq = max(m_seq, seq)
        seq = 1
        l = i

print(max(m_seq, seq))