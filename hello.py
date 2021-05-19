import random

names = ["marko", "pero", "djuro"]
sign = [".", "-", "_"]
nick = ["djetlic", "legenda", "smrad"]
domena = ["@hotmail.com", "@gmail.com", "@yahoo.com"]

output_list = []

def compose():
	for x in range(0,6):
		output = names[random.randint(0,2)] + sign[random.randint(0,2)] + nick[random.randint(0,2)] + domena[random.randint(0,2)]
		output_list.append(output)
	print(output_list)

compose()