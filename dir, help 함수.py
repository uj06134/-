import pandas as pd
# dir 함수
print(dir(pd))
print(dir(pd.DataFrame))

# help 함수
print(help(pd.DataFrame.fillna))

# __all__
import sklearn
print(sklearn.__all__)
print(sklearn.preprocessing.__all__)