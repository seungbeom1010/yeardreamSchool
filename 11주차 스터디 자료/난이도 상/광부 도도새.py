N, T, P = map(int, input().split())
coal_list = [int(x) for x in input().split()]

m_coal = []

for i in range(N):
    m_coal.append(coal_list[i] + P * i)

print(m_coal)