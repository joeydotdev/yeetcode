src,dst,ratio

usd,btc,9000
btc,eth,10



usd: [ ['btc', 9000], [...], [..] ]
btc: [ ['usd', ...], [...], ..]

wanting:
usd -> eth



def dfs(current_currency, ending_currency, list, visited, path):
	"""
		set = []
	
		grab all the vals our current currency supports:
			check if our current currency contains end currency:
				return [path, multiply(path)]

	"""
	pass


usd -> btc -> eth
usd -> ltc -> dogecoin -> eth

def get_ratio(starting_currency, ending_currency):
	# populate the adjacency list


	"""
		check if on our list['usd'] contains ending_currency
			if does
				return that ratio
			else
				take first val in the list,
				perform a dfs
				return dfs(btc, eth, list, [usd]) if val was non error

				current_currency -> first_value -> dfs(...)
	"""
	set()
	pass

def find_ratio(csv):
	"""
		src,dest,val
		list = {'usd': [ {'btc': 9000}, {'eth': 500} ], 'btc': [ {'usd': 1/9000 }, {'eth': 200} ]}
	"""	
	rows = csv.split("\n")
	adjacency_list = {}
	for row in rows:
		src, dest, val = rows.split(",")
		if src not in adjacency_list:
			adjacency_list[src] = []

		adjacency_list[src].append({dest: val})

		if dest not in adjacency_list:
			adjacency_list[dest] = []

		adjacency_list[dest].append({src: 1/val})

	return adjacency_list