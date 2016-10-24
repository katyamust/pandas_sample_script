import pandas as pd
import numpy as np

def compare(df1, df2):
    #df_pred_2 = df_predicted.rename(columns={'User': 'ExternalId', 'Item': 'CouponId'}, inplace=True)

    merged = df1.merge(df2, how='left', indicator=True)
    both_df = merged[merged['_merge'] == 'both']
    print(both_df.shape)

    left_df = merged[merged['_merge'] == 'left']
    print(left_df.shape)


if __name__ == "__main__":
    df1 = pd.DataFrame(np.random.randint(0,100,size=(100, 9)), columns=list('ABCDEFGHK'))
    #df2 = df1.copy()
    df2 = pd.DataFrame(np.random.randint(222,22222,size=(100, 9)), columns=list('ABCDEFGHK'))


    #x = np.array(range(0, n))

    compare(df1,df2)

# # compare datafraem @@ check if one datareame contain in another etc
# print("Compare predicted and actial datasets")
#
# df_pred_2 = df_predicted.rename(columns={'User': 'ExternalId', 'Item': 'CouponId'}, inplace=True)
# df_pred_2 = df_pred_2[['User', 'Item']]
#
# ....
# df_actual_2 = df_actual[['ExternalId', 'CouponId']]
#
# merged = df_actual_2.merge(df_pred_2, how='left', indicator=True)
#
# both_df = merged[merged['_merge'] == 'both']
# print(both_df.shape)


# #print(both_df.head(5))
#
#
# diff_user = df_actual['ExternalId'] == df_predicted['User']
# diff_item = df_actual['CouponId'] == df_predicted['Item']
#
# same = (diff_item.unique() == 1 and diff_item[0] == True) and   (diff_user.unique() == 1 and diff_user[0] == True)
#
# print("Data sets are identical :")
# print(same)
#
# print("Compare test and traning sets")
# print("<User, Item> pairs  of test set contained in training set:")
#
# df_traning_2 = df_traning[['ExternalId', 'CouponId']]
# df_actual_2 = df_actual[['ExternalId', 'CouponId']]
#
# merged = df_actual_2.merge(df_traning_2, how='left', indicator=True)
#
# both_df = merged[merged['_merge'] == 'both']
# print(both_df.shape)
# # #print(both_df.head(5))
#
# print("<User> of test set contained in training set:")
# df_traning_22 = df_traning[['ExternalId']]
# df_actual_22 = df_actual[['ExternalId']]
#
# merged2 = df_actual_22.merge(df_traning_22, how='left', indicator=True)
#
# both_df = merged2[merged2['_merge'] == 'both']
# print(both_df.shape)
# # print(both_df.head(5))

# df_actual_2_test = df_actual[['ExternalId', 'CouponId']]
# df_actual_2_test.rename(columns={'ExternalId': 'User', 'CouponId': 'Item'}, inplace=True)

# df_predicted_2 = df_predicted[['User', 'Item']]
# merged_test = df_actual_2_test.merge(df_predicted_2, how='left', indicator=True)

# both_df_test = merged_test[merged_test['_merge'] == 'both']

# merged = df.merge(other, how='left', indicator=True)

#
# print('Grouping')
# actual_members = df_actual.groupby(df_actual['ExternalId', 'CouponId'])
#
# predicted_members = df_predicted.groupby(df_predicted.User)
# traning_members = df_traning.groupby(df_traning.ExternalId)
# #
# actual_dict = {}
# actual_dict.update(actual_members.groups)
# #
# # predicted_dict = {}
# # predicted_dict.update(predicted_members.groups)
# #
# traning_dict = {}
# traning_dict.update(traning_members.groups)
#
# for key in actual_dict.keys():
#     try:
#         member_found = traning_dict[key]
#         train_ratings  = df_traning[df_traning.ExternaId == member_found]
#
#         print("found")
#         print(found)
#     except KeyError:
#         pass