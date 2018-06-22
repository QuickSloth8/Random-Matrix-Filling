import random
import time
import os

def insert_to_str_random(curr_str):
	while True:
		c = chr(random.randint(33, 64))
		if not c.isdigit() and c != ' ' and c != '':
			break

	if len(curr_str) > 1 and random.uniform(0, 1) > 0.9:
		while True:
			new_line_index = random.randint(1, len(curr_str)-1)
			if curr_str[new_line_index] != '\n' and (new_line_index ==len(curr_str)-1 or curr_str[new_line_index+1] != '\n') and not (new_line_index ==len(curr_str)-1 and curr_str[new_line_index+1] != '\n'):
				curr_str = curr_str[:new_line_index] + '\n' + curr_str[new_line_index:]
				break

	insertion_index = random.randint(0, len(curr_str))
	return curr_str[:insertion_index] + c + curr_str[insertion_index:]

def main():
	curr_str = ''
	TITLE = "**** RANDOM DRAWING ****"

	while True:
		curr_str = insert_to_str_random(curr_str)
		os.system('cls')
		print(TITLE, end='\n\n')
		print(curr_str)
		time.sleep(random.uniform(0.001, 0.2))

if __name__ == "__main__":
	main()