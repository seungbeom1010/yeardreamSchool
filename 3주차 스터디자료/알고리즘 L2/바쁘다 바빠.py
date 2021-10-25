m_times = 0

for i in range(4):
    m_times += int(input()) #이동 시간 총합 구하기

min = m_times // 60 
sec = m_times % 60

print(min, sec, sep='\n')
