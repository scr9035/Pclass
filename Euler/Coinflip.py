
def create_change_list(change, coin_values):
	change_list = []
	coin_values.sort()
	coin_values.reverse()
	i=0
	
	for i in range(0,change+1):
		for coin in coin_values:
			if i%coin == 0:
				change_list.append(coin)
				break
	print change_list
	return change_list

def make_change(change, coin_values):
	coin_list = []
	change_list = create_change_list(change, coin_values)
	while change > 1:
		coin_list.append(change_list[change])
		change = change - change_list[change]
	return coin_list


coin_demon = [1,5,10,25]
money = 37


test = make_change(money,coin_demon)


print test
