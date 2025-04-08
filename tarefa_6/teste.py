import pandas as pd

df = pd.read_csv('/home/candim/Downloads/california_housing_test.csv')

df_1 = df[['longitude', 'latitude', 'median_income']].iloc[0:10].copy()
df_2 = df[['longitude', 'latitude', 'median_income']].iloc[10:20].copy()
df_3 = df[['longitude', 'latitude', 'median_income']].iloc[20:30].copy()

df_vertical = pd.concat([df_1, df_2, df_3], axis=0)

df_horizontal = pd.concat([df_1, df_2, df_3], axis=1)

df_1['company_location'] = ['A'] * 10
df_2['company_location'] = ['A'] * 5 + ['B'] * 5

df_merge_inner = pd.merge(df_1, df_2, on='company_location', how='inner')

df_merge_left = pd.merge(df_1, df_2, on='company_location', how='left')
df_merge_right = pd.merge(df_1, df_2, on='company_location', how='right')
df_merge_outer = pd.merge(df_1, df_2, on='company_location', how='outer')

df_merge_inner.to_csv('merge_inner_result.csv', index=False)
df_merge_left.to_csv('merge_left_result.csv', index=False)
df_merge_right.to_csv('merge_right_result.csv', index=False)
df_merge_outer.to_csv('merge_outer_result.csv', index=False)

