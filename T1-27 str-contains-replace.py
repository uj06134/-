# 바닐라라떼 5점, 카페라떼 3점, 아메리카노 2점, 나머지 0점이다 총 메뉴의 점수를 더한 값은?
import pandas as pd
df = pd.read_csv("data/payment.csv")
# print(df)

# # 전처리
# df.loc[df['menu'] == '카페 라떼', 'menu'] = '카페라떼'
#
# # 메뉴 점수
# df.loc[df['menu'] == '바닐라라떼', 'score'] = 5
# df.loc[df['menu'] == '카페라떼', 'score'] = 3
# df.loc[df['menu'] == '아메리카노', 'score'] = 2
# df.loc[(df['menu'] != '바닐라라떼') & (df['menu'] != '카페라떼') & (df['menu'] != '아메리카노'), 'score'] = 0
#
# # 결과
# result = df['score'].sum()
# print(result)


# 풀이
df['menu'] = df['menu'].str.replace(' ','')
s1 = sum(df['menu'].str.contains("바닐라라떼"))
s2 = sum(df['menu'].str.contains("카페라떼"))
s3 = sum(df['menu'].str.contains("아메리카노"))
print((s1*5) + (s2*3) + (s3*2))