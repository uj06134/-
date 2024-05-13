# city와 f4를 기준으로 f5의 평균값을 구한 다음, f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
import pandas as pd
df = pd.read_csv("data/basic1.csv")
# print(df)

# city와 f4를 기준으로 f5의 평균값 구하기
df = df.groupby(by = ['city', 'f4'])['f5'].mean()
# print(df)

# dataframe 전환 후 상위 7개 출력
df = df.reset_index().sort_values('f5', ascending=False).head(7)
# print(df)

# f7의 합계 (소수점 둘째자리까지)
result = round(df['f5'].sum(), 2)
print(result)

# reset_index() 메서드를 사용하지 않아도 되는 이유
# groupby() 함수를 사용하여 그룹화하면 그룹화된 열은 인덱스로 유지됩니다. 즉, city와 f4 열이 인덱스가 되어 있기 때문에,
# 이 인덱스를 유지한 채로 평균값을 계산하고, sort_values() 함수를 사용하여 정렬할 수 있습니다.
print(round(df.groupby(by=['city', 'f4'])['f5'].mean().sort_values(ascending=False).head(7).sum(), 2))