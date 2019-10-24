import pandas as pd
from test_data import get_test_row


def get_median_price(property_name, room_name, date, month):

    icon = pd.read_csv('train.csv')

    comp_list = []

    train_X = icon[['property', 'room', 'date', 'month', 'amount']]
    train_frame = train_X.groupby(['property', 'month', 'date', 'room']).median()

    for i in train_frame.index:

        lis = []

        for item in i:
            lis.append(item)

        comp_list.append(lis)

    count = 0
    test_list = get_test_row(property_name, room_name, date, month)
    # test_list = [2, 6, 36, 2]

    for j in comp_list:
        if test_list == j:
            break

        else:
            print("no match found for test data")
            pass

        count += 1

    # price = train_frame.iloc[count]
    # price = price[0]

    train_frame_reset = train_frame.reset_index()
    m_price = train_frame_reset.iloc[count]['amount']

    return m_price

