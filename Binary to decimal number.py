#the custom exception for when the input isn't a binary number
class NonBinaryError(Exception):
    pass


while True: #the while loop will ensure the code loops through all code correctly
    try:
        #get the input of the binary number you want converted to decimal
        num = int(input('Type in your binary number: ')) 
        binary = [int(x) for x in str(num)]
        for x in binary:
            if x > 1:
                raise NonBinaryError #calls the custom exception for non-binary numbers
       
    except NonBinaryError:
        print('The number is non-binary, input an actual binary number.')

    #This exception takes care of other non-integer inputs like letters and symbols
    except Exception: 
        print('Invalid input, type in your binary number: ')

    #The code proceeds when no error is raised so far
    else: 
        def bin_to_dec(binary):
            binary.reverse()
            while binary:
                bin_len = len(binary)
                dec_num = 0
                for i in range(bin_len):
                    x = 2**i
                    if binary[0]:
                        dec_num += x
                    else:
                        dec_num += 0
                    del binary[0]   
                        
            return dec_num
        
        #We call our function to convert the binary number input into a decimal number
        #and print out the results in a statement
        res = bin_to_dec(binary) 
        print(f'Your binary number {num} returns the decimal number {res}')
        
        break #The while loop closes successfully

