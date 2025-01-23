import pandas as pd

# 假设你已经加载了你的原始数据到一个名为df的DataFrame中。
df = pd.read_csv('D:\pycharm\FinDoctor\Wind_data\data\data_all.csv')  # 请替换为你的实际文件路径

# 示例数据
# data = {
#     "code": ["000061.SZ"] * 9,
#     "名称": ["农产品"] * 9,
#     "source": ["Shenzhen Agricultural Products Group Co., Ltd."] * 9,
#     "target": ["Nanchang Shennong Cold Chain Logistics Co., Ltd."] * 9,
#     "担保方公司名称": ["深圳市农产品集团股份有限公司"] * 9,
#     "被担保方公司名称": ["南昌深农冷链物流有限公司"] * 9,
#     # ... 其他列 ...
# }

# 创建DataFrame
#df = pd.DataFrame(data)

# 获取所有涉及的公司名称，并确保它们是唯一的
all_companies = set(df['source']).union(set(df['target']))

# 创建一个新的DataFrame来存储公司ID和名称
company_df = pd.DataFrame({
    'companyId': range(1, len(all_companies) + 1),
    'companyName': list(all_companies)
})
# 将 company_df 与原始数据中的 default 和 category 列合并
# 首先为每个公司创建一个带有 default 和 category 的 DataFrame
company_details = []

for name in all_companies:
    # 取得该公司在原始数据中出现的任意一行的 default 和 category 值
    sample_row = df[(df['source'] == name) | (df['target'] == name)].iloc[0]
    default_val = sample_row['default']
    category_val = sample_row['category']

    company_details.append({
        'companyId': company_df[company_df['companyName'] == name]['companyId'].values[0],
        'companyName': name,
        'default': default_val,
        'category': category_val
    })

# 创建最终的DataFrame
final_df = pd.DataFrame(company_details)

# 保存到CSV文件
final_df.to_csv('wind_node.csv', index=False)

print("CSV 文件已保存")
