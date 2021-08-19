

def get_players_name():
	while(True):
		first_player=input("Введите имя первого  игрока:")
		second_player=input("Введите имя второго  игрока:")
		if first_player!=second_player:
			return (first_player, second_player)
		else:
			print("Ошибка! Имена играков не могут совпадать!!")


def is_game_over(table_cells):
	if '-' not in table_cells.values():
		return 3
	win_first = "+++"
	win_second = "ooo"
	res_1 = ""
	res_2 = ""
	for i in range(3):
		for j in range(3):
			res_1+=table_cells[(i,j)]	
			res_2+=table_cells[(j,i)]
		if res_1==win_first or res_2==win_first:
			return 0
		elif res_1 == win_second or res_2 == win_second:
			return 1
		
		res_1 = ""
		res_2 = ""
	
	res_1 = ""
	res_2 = ""
	for i in range(3):
		res_1+=table_cells[(i,i)]
	for i, j in [(0,2),(1,1),(2,0)]:
		res_2+=table_cells[(i,j)]
	if res_1==win_first or res_2==win_first:
			return 0
	elif res_1 == win_second or res_2 == win_second:
			return 1

	return None

def print_table(table_cells):
	game_table = """
	   0 1 2
	0  {} {} {}
	1  {} {} {}
	2  {} {} {}
	""".format(table_cells[(0,0)],table_cells[(0,1)],table_cells[(0,2)],
			   table_cells[(1,0)],table_cells[(1,1)],table_cells[(1,2)],
			   table_cells[(2,0)],table_cells[(2,1)],table_cells[(2,2)], )

	print(game_table)

def game_start(players):
	print("""Ходы вводятся в формате "i:j" где 
		i - номер строки
		j - номер столбца """)
	i = 0
	table_cells ={
		(0,0):'-',
		(0,1):'-',
		(0,2):'-',
		(1,0):'-',
		(1,1):'-',
		(1,2):'-',
		(2,0):'-',
		(2,1):'-',
		(2,2):'-',
		}
	print_table(table_cells)
	while(True):
		
		
		if i%2==0:
			next_step = input(f"Ход игрока {players[0]}: ")
			next_step =tuple(map(int,next_step.split(':')))
			table_cells[next_step] = '+'
		else:
			next_step = input(f"Ход игрока {players[1]}: ")
			next_step =tuple(map(int,next_step.split(':')))
			table_cells[next_step] = 'o'
		print_table(table_cells)
		win = is_game_over(table_cells)
		if win is not None:
			try:
				return players[win]
			except:
				return "дружба"

		i+=1



if __name__ == "__main__":
	players = get_players_name()
	winner = game_start(players)
	print(f" Победил игрок {winner}")
