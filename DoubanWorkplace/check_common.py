import pandas as pd

a = pd.read_csv("merge_6678072_688259.csv")
b = pd.read_csv("members_690472.csv")

output = a.merge(b,on='user_page').fillna(0)
output.to_csv("merge_except_curleyg.csv")