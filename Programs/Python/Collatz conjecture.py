print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n|Weirdo's Collatz conjecture|\n|by CoolTrainerEX           |\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
again = 1
while (again == 1):
	num = input("\nType a natural number: ")
	try:
	    num = int(num)
	except:
	    print("It must be an integer\n")
	else:
	    if (num < 1):
	        print("It must be positive.\n")
	    else:
	        i = 0
	        stop = 0
	        again = 2
	        print()
	        while (stop != 2):
	            if (num % 2 == 1):
	                num = num * 3 + 1
	            else:
	                num //= 2
	            i += 1
	            if (num == 1):
	                stop += 1
	            print(num)
	        print("\n" + str(i),"steps")
	        while (not(again == 0 or again == 1)):
	            again = input("\nWould you like to try again?\n[1] = yes\n[0] = no\nChoice: ")
	            if (not(again == "0" or again == "1")):
	                print("It can only be either 1 or 0")
	            else:
	                again = int(again)