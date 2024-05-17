# f1의 결측치를 채운 후 age 컬럼의 중복 제거 전과 후의 'f1' 중앙값 차이를 구하시오
# - 결측치는 f1의 데이터 중 10번째로 큰 값으로 채움
# - 중복 데이터 발생시 뒤에 나오는 데이터를 삭제함
# - 최종 결과값은 절대값으로 출력
import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df)

# f1데이터에서 10번째 큰 값으로 결측치를 채움
top10 = df['f1'].sort_values(ascending=False).iloc[9]
# print(top10)
df['f1'] = df['f1'].fillna(top10)

# 중복 제거 전의 중앙값
med1 = df['f1'].median()

# 중복 제거
# drop_duplicates(subset=['col']): 컬럼 중복 제거
df = df.drop_duplicates(subset=['age'])

# 중족 제거 후의 중앙값
med2 = df['f1'].median()

# 중복 제거 전과 후의 'f1' 중앙값 차이
result = abs(med1 - med2)
print(result)
