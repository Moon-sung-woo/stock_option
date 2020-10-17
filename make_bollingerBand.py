import pandas as pd
import matplotlib.pyplot as plt

w_size = 20 # 볼린져밴드 이동평균 산출 기간
pb = 2      # 볼린져밴드 승수(percent bendwidth)
stock_csv = '005380.csv'

data = pd.read_csv(stock_csv)
range = pd.date_range('1990-01-04', '1991-01-01', freq='1D')
end_data = data['종가']

data['Moving Average'] = end_data.rolling(window=w_size, min_periods=1).mean()
data['Standard Deviation'] = end_data.rolling(window=w_size, min_periods=1).std()
data['UBB'] = data['Moving Average'] + (data['Standard Deviation'] * pb)
data['LBB'] = data['Moving Average'] - (data['Standard Deviation'] * pb)

print(end_data)

data.to_csv('test.csv') # 지끔까지 추가한것들 저장

data[['종가', 'UBB', 'LBB']].plot()
plt.show()