def main():
    plist = []
    ##################################################
    # Comlete your code here 
    ##################################################
    def is_prime(num):
        if num == 2:
            return True
        if num <= 1 or num % 2==0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True
                
        
    begin = int(input("Enter an integer value greater than 1: "))
    end = int(input("Enter an integer value greater than the last input: "))
    
    if begin >= end:
        print("Invalid input; The second number must be greater than the first.")
    elif begin <=1 or end <=1:
        print("Invalid input; The integers must be greater than 1.")
    else:
        for num in range(begin,end+1):
            if is_prime(num):
                plist.append(num)
                
    print(plist)
    return plist


if __name__ == '__main__':
    main()
