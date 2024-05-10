# 주어진 데이터에서 상관관계를 구하고, quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 출력
import pandas as pd
df = pd.read_csv("data/winequality-red.csv")
# print(df)

# 상관관계 구하기
df_corr = df.corr()
# print(df_corr)

# quality와 quality 상관관계 제외하고 구하기
df_corr = df_corr[:-1]
# print(df_corr)

# 상관관계가 가장 큰 값과 가장 작은 값 (절대값으로 확인)
max_corr = abs(df.corr()['quality'][:-1]).max()
min_corr = abs(df.corr()['quality'][:-1]).min()

if max_corr not in df.corr()[['quality']][:-1].values:
    max_corr=-max_corr
if min_corr not in df.corr()[['quality']][:-1].values:
    min_corr=-min_corr

# 결과 출력
result = round(max_corr + min_corr, 2)
print(result)