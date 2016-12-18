from sys import argv

def main(argv):
	filename_names = argv[1]
	filename_source = argv[2]
	names = {}
	with open(filename_names) as f:
		for line in f:
			names[line.strip("\n")] = 0
	with open(filename_source) as f:
		for line in f:
			for word in line.split():
				word = word.strip("\n")
				if word in names:
					names[word] = names[word] + 1
	for name in names:
		print(name+": "+str(names[name]))

if __name__ == "__main__":
	main(argv)