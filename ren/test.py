for i in range(1, 101):
	name = str(i)
	name = name + ".txt"
	print(name)
	print(type(name))
	arq = open(name, "w")
	arq.close();
