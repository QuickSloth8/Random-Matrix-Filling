import random
import time
import sys
import os

ROWS = 0
COLS = 0

ascii_mat = []
display_mat = []

def main():
	get_ascii_mat('Einstein_tongue (60).txt')
	random_draw()

	# cls()
	# for i in range(ROWS):
	# 	print(' '*10, end='')
	# 	for j in range(COLS):
	# 		print(ascii_mat[i][j], end='')
	# 	print('\n', end='')

def get_ascii_mat(file_name):
	global ascii_mat
	tmp_ascii_mat = []
	max_line_len = 0
	lines_no = 0

	with open(file_name) as ascii_file:
		for line in ascii_file:
			line = line.replace('\n', '')
			tmp_ascii_mat.append(line)
			max_line_len = max(max_line_len, len(line))
			lines_no += 1

	global ROWS, COLS
	ROWS = lines_no
	COLS = max_line_len

	for i in range(len(tmp_ascii_mat)):
		while len(tmp_ascii_mat[i]) < max_line_len:
			tmp_ascii_mat[i] += ' '

	for i, line in enumerate(tmp_ascii_mat):
		ascii_mat.append([])
		for j in range(len(line)):
			ascii_mat[i].append(line[j])

	init_display_mat()

def init_display_mat():
	global display_mat

	for i in range(ROWS):
		display_mat.append([])
		for j in range(COLS):
			display_mat[i].append(' ')

def print_display_mat():
	cls()
	for i in range(ROWS):
		print(' '*10, end='')
		for j in range(COLS):
			print(display_mat[i][j], end='')
		print('\n', end='')

def random_draw():

	coordinates_lst = []

	for i in range(ROWS):
		for j in range(COLS):
			coordinates_lst.append((i, j))

	while coordinates_lst != []:
		rand_i, rand_j = random.choice(coordinates_lst)
		coordinates_lst.remove((rand_i, rand_j))

		display_mat[rand_i][rand_j] = ascii_mat[rand_i][rand_j]

		print_display_mat()

def cls():
	a = os.system('cls')

if __name__ == "__main__":
	main()