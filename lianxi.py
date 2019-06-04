import warnings
import numpy as np
import pandas as pd
import os

#这是无视警告的代码
warnings.filterwarnings('ignore')
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'


# df1=pd.DataFrame([[1,1],[2,2],[3,3],[4,4]],columns=['aa','bb'])
# df2=pd.DataFrame([[2,2],[2,3],[3,3],[4,4],[5,5]],columns=['aa','cc'])
# df3=pd.merge(left=df1,right=df2,how='left',on='aa')
# print(df3)

df_barcode=pd.read_excel('../关联表/barcode-0422.xls',sheet_name='使用中')
count1=df_barcode.条形码.value_counts()
# num1=len(df_barcode)
# num2=len(df_barcode.条形码.unique())
print(count1)