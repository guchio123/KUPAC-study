print("-----------------------------------------------------------------------------------------------------------")


# 関数の定義
def fruit_price(number_of_momo, number_of_mikan):
    # ももとみかんの合計金額を計算する

    total_momo = number_of_momo * 100
    total_mikan = number_of_mikan * 40
    total = total_momo + total_mikan
    return total



# もも5個、みかん10個の値段を計算
total = fruit_price(5, 10)
print("もも 5個と、みかん 10個で、", total, "円です")


print("-----------------------------------------------------------------------------------------------------------")
