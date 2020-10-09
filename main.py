from bruteforce import Bruteforce
from sieve_of_eratosthenes import SieveOfEratosthenes

if __name__=='__main__':
    while True:
        print("""\nWhich program to run: 
1) SieveOfEratosthenes 
2) Brute-Force 
3) Exit""")
        run = input("\nPlease Enter your choice: ")
        if run == "1" or run == "SieveOfEratosthenes":
            print(*SieveOfEratosthenes(int(input("\nEnter the max number: "))))
        elif run == "2" or run == "Bruteforce" or run == "Brute-Force":
            print(*Bruteforce(int(input("\nEnter the max number: "))))
        elif run == "3" or run == "exit":
            break
        else:
            print("\nError. Please enter 1, 2, or 3")
