# 주어진 데이터에서 상관관계를 구하고, quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 출력
import pandas as pd
df = pd.read_csv("data/winequality-red.csv")
# print(df)

# 상관관계가 가장 큰 값과 가장 작은 값 (절대값으로 확인)
max_corr = abs(df.corr()['quality'][:-1]).max()
min_corr = abs(df.corr()['quality'][:-1]).min()

# if 절을 사용하여 최종적으로 계산된 값이 원래의 상관관계 값과 부호가 같도록 조정
if max_corr not in df.corr()[['quality']][:-1].values:
    max_corr=-max_corr
if min_corr not in df.corr()[['quality']][:-1].values:
    min_corr=-min_corr

# 결과
result = round(max_corr + min_corr, 2)
print(result)