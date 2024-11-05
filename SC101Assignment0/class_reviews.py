"""
File: class_reviews.py
Name: 黃方易
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1


def main():
    """
    TODO: 讓使用者班級打SC001 or SC101，並輸入成績加總算出最大值/最小值/平均值
    """
    c = str(input('Which class: '))   # c=class，請輸入SC001 or SC101
    d = 'SC001'
    d1 = 'sc001'                      # 在大小寫的常數都考量進去
    d2 = 'Sc001'
    d3 = 'sC001'
    f = 'SC101'
    f1 = 'sc101'
    f2 = 'Sc101'
    f3 = 'sC101'
    times = 0     # 輸入 SC001 次數
    times_f = 0   # 輸入 SC101 次數
    while True:
        if c == str(EXIT):                   # 若在課堂輸入-1，回覆無此課程
            break
        else:
            if c == d or c == d1 or c == d2 or c == d3:
                score = int(input('Score: '))
                if times == 0:                  # 第一次成績輸入
                    max_score = score
                    min_score = score
                    total_score = score
                else:                           # 第2次以後的成績輸入，並馬上大小
                    if score > max_score:
                        max_score = score
                    if score < min_score:
                        min_score = score
                    total_score += score
                times += 1                       # 次數都需要+1
            elif c == f or c == f1 or c == f2 or c == f3:
                score_f = int(input('Score: '))
                if times_f == 0:
                    max_score_f = score_f
                    min_score_f = score_f
                    total_score_f = score_f
                else:
                    if score_f > max_score_f:
                        max_score_f = score_f
                    if score_f < min_score_f:
                        min_score_f = score_f
                    total_score_f += score_f
                times_f += 1
            c = str(input('Which class: '))
    if times == 0 and times_f == 0:
        print('No class scores were entered.')
    else:
        if times == 0:                              # 若次數0，代表都沒有，就顯示沒成績
            print('=' * 13 + 'SC001' + '=' * 13)
            print('No scores for ' + 'SC001')
        else:
            print('='*13 + 'SC001' + '='*13)
            print('Max(001):' + str(max_score))
            print('Min(001):' + str(min_score))
            print('Avg(001):' + str(total_score/times))
        if times_f == 0:
            print('=' * 13 + 'SC101' + '=' * 13)
            print('No scores for ' + 'SC101')
        else:
            print('=' * 13 + 'SC101' + '=' * 13)
            print('Max(101):' + str(max_score_f))
            print('Min(101):' + str(min_score_f))
            print('Avg(101):' + str(total_score_f / times_f))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
