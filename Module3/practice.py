# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

secret_num = 80
while True:
    num = int(input("請輸入1~100: "))
    if num == secret_num:
        print("恭喜中獎")
        break
    elif num > 100 or num < 1:
        print("超出範圍請重新輸入")
    elif num > secret_num:
        print("請輸入更小的數字")
    elif num < secret_num:
        print("請輸入更大的數字")

   

