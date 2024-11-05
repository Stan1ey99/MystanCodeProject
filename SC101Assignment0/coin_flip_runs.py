"""
File: coin_flip_runs.py
Name: 黃方易
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r

# 將數字轉換成英文


def number_to_letters(number):
	if number == 1:
		return 'H'
	elif number == 2:
		return 'T'
	else:
		pass


def main():
	"""
	輸入次數，分別英文 T or H 印出，輸入到重疊  #參考期末的畫面
	"""
	print("Let's flip a coin!")  # 印出來字樣
	n = int(input('Number of runs: '))  # 給使用者輸入數字，並且代表為重複的數字
	run = 0
	flip1 = r.randint(1, 2)
	can_add = True
	while True:						# 運用骰子的方式，做開關
		flip2 = r.randint(1, 2)
		if flip1 == flip2:
			if can_add:
				run += 1
				can_add = False
		else:
			can_add = True
			if run == n:
				break
		flip1 = flip2
		print(number_to_letters(flip1), end='')
	print(number_to_letters(flip2), end='')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #


if __name__ == "__main__":
	main()
