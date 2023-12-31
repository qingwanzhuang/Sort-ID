import pandas as pd


path = r"C:\Users\wanqing\Desktop\coding\table.csv"
df = pd.read_csv(path)
print(df.info())

# 1. sort pandas.dataframe by 編號
# 2. output csv in same csv File


def sort_csv(input_file, output_file, sort_column):
    # 读取CSV文件
    df = pd.read_csv(input_file)

    # 按照指定列排序
    sorted_df = df.sort_values(by=sort_column)

    # 将排序后的数据写回CSV文件
    sorted_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = r"C:\Users\wanqing\Desktop\coding\table.csv"  # 替换为你的输入CSV文件路径
    output_file = r"C:\Users\wanqing\Desktop\coding\table.csv"  # 替换为你的输出CSV文件路径
    sort_column = "編號"  # 按照編號列进行排序

    sort_csv(input_file, output_file, sort_column)
    print("CSV已排序并保存为", output_file)