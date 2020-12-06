import pandas as pd
import matplotlib.pyplot as plt

stock_data = pd.read_excel('stock_table.xlsx', sheet_name='Sheet1')

stock_data['시가'].plot(kind='bar')
plt.show(block=True)