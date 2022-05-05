# -*- coding : utf-8-*-

import pandas as pd


# 查看原始的训练集
def show_original_data():
    file_path = '../data/train.csv'

    with open(file_path, 'rb') as f:
        result = f.readlines()
        print(len(result))
        byte_arr = result[87]
        print(byte_arr)
        print(byte_arr[111:114])
        print(byte_arr.decode('utf-8'))


# 数据清洗
def revise_train_csv():
    train_data = pd.read_csv('../data/train.csv')
    print(train_data.info())
    # 删除多出数据的行
    overflow = train_data['Unnamed: 17'].isnull()
    rows = []
    for i in range(len(overflow)):
        if not overflow[i]:
            rows.append(i)
    new_data = train_data.drop(labels=rows)
    columns = []
    for i in range(17, 48):
        columns.append('Unnamed: ' + str(i))
    new_data.drop(labels=columns, axis=1, inplace=True)
    # 处理缺少target的数据
    new_data.dropna(subset=['target'], inplace=True)
    print(new_data.info())
    new_data.to_csv('../data/new_train.csv', index=0)


def observe_test_data():
    test_data = pd.read_csv('../data/test.csv')
    print(test_data.info())


def get_description():
    train_description = pd.read_csv('../data/new_train.csv', usecols=[0])
    train_description.to_csv('../data/train_description.csv', index=0)
    test_description = pd.read_csv('../data/test.csv', usecols=[0])
    test_description.to_csv('../data/test_description.csv', index=0)


if __name__ == '__main__':
    observe_test_data()
    get_description()
    # revise_train_csv()
