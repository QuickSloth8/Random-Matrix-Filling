import random
import time
import sys
import os

ROWS = 10
COLS = 20

bcolors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m']
ENDC = '\033[0m'
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'    

chars_mat = []
colors_mat = []
cells_no = 0

def init_chars_mat():
	global cells_no, chars_mat, ROWS, COLS

	if len(sys.argv) == 3:
		ROWS = int(sys.argv[1])
		COLS = int(sys.argv[2])

	cells_no = ROWS * COLS - (2*ROWS + 2*COLS - 4)
	for i in range(ROWS):
		chars_mat.append([])
		colors_mat.append([])
		for j in range(COLS):
			chars_mat[i].append(' ')
			colors_mat[i].append('\033[1m')
	for i in range(0, ROWS):
		chars_mat[i][0] = chars_mat[i][COLS-1] = '|'
	for j in range(0, COLS):
		chars_mat[0][j] = chars_mat[ROWS-1][j] = '-'

def print_chars_mat():
	for i in range(ROWS):
		for j in range(COLS):
			print('%s%s%s' % (colors_mat[i][j], chars_mat[i][j], ENDC), end='')
		print('\n', end='')

def random_insert_to_chars_mat():
	global cells_no

	while True:
		insert_i = random.randint(1, ROWS-2)
		insert_j = random.randint(1, COLS-2)
		if chars_mat[insert_i][insert_j] == ' ':
			cells_no -= 1
			break

	chars_mat[insert_i][insert_j] = chr(random.randint(33, 64))
	colors_mat[insert_i][insert_j] = bcolors[random.randint(0, len(bcolors)-1)]

def cls():
	a = os.system('cls')

def main():
	global cells_no
	init_chars_mat()

	while cells_no > 0:
		random_insert_to_chars_mat()
		cls()
		print('')
		print_chars_mat()
		print(cells_no)
		time.sleep(0.333)

if __name__ == "__main__":
	main()