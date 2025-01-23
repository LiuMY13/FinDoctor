import pandas as pd

# 加载公司信息，包括公司ID和名称
company_df = pd.read_csv('wind_node.csv')

# 创建公司名称到ID的映射字典
company_mapping = {row['companyName']: row['companyId'] for index, row in company_df.iterrows()}

# 加载原始数据
df = pd.read_csv('D:\pycharm\FinDoctor\Wind_data\data\data_all.csv')

# 添加source_id和target_id列，使用公司名称映射到ID
df['source_id'] = df['source'].map(company_mapping)
df['target_id'] = df['target'].map(company_mapping)

# 确保所有的source和target都能正确映射到ID，如果没有映射到则删除该行
df.dropna(subset=['source_id', 'target_id'], inplace=True)

# 将source_id和target_id转换为整数类型
df['source_id'] = df['source_id'].astype(int)
df['target_id'] = df['target_id'].astype(int)

# 保存带有新列的DataFrame到新的CSV文件
output_path = 'wind_edge.csv'
df.to_csv(output_path, index=False)

print(f"Updated CSV 文件已保存到: {output_path}")