# 計算幾次方
def pow(x, y):
    return x**y


# 簡單斷句
def segment_sentence(text):
    list_sentences = text.split(' ')
    return list_sentences

if __name__ == "__main__":

    # 測試模組
    result = pow(2, 3)
    print(result)

    text = "I will always love you"
    text_result = segment_sentence(text)

    print(text_result)

