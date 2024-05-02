# 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고,
# 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요
import pandas as pd
df = pd.read_csv("data/basic1.csv")
# print(df)

# 결측치 합계
# print(df.isnull().sum())

# 결측비율 확인
# print(df.isnull().sum()/df.shape[0])

# 결측치가 80% 이상 되는 컬럼 f3 삭제
df = df.drop(['f3'], axis=1)
# print(df)

# 도시 확인
# print(df['city'].unique())

# 도시별 중앙값 구하기
med_s = df.loc[df['city']=='서울', 'f1'].median()
med_g = df.loc[df['city']=='경기', 'f1'].median()
med_b = df.loc[df['city']=='부산', 'f1'].median()
med_d = df.loc[df['city']=='대구', 'f1'].median()

# print(med_s, med_g, med_b, med_d)

# f1결측치 city별 중앙값으로 대체
# map 활용
df['f1'] = df['f1'].fillna(df['city'].map({'서울':med_s,'경기':med_g,'부산':med_b,'대구':med_d}))

# replace 활용
df['f1'] = df['f1'].fillna(df['city'].replace({'서울': med_s, '경기': med_g, '부산': med_b, '대구': med_d}))

# 'f1'컬럼의 평균값을 출력
result = df['f1'].mean()
print(result)
