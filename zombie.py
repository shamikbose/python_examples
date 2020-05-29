def main():
	n=raw_input()
	clusters=1
	list1=[]
	for i in range(int(n)):
		for x,y in enumerate(raw_input()):
			if(y=='1'):
				list1.append(x)
			
	#print list1


if __name__ == '__main__':
	main()