#the custom exception for when the input isn't a binary number
class NonBinaryError(Exception):
    pass


while True: #the while loop will ensure the code continues regardless
    try:
        #get the input of the binary number being converted to decimal
        num = int(input('Type in your binary number: ')) 
        binary = [int(x) for x in str(num)]
        for x in binary:
            if x > 1:
                raise NonBinaryError #calls the custom exception for non-binary numbers
       
    except NonBinaryError:
        print('The number is non-binary, input an actual binary number.')

    except Exception: #This exception takes care of other non-integer inputs
        print('Invalid input, type in your binary number: ')

    else: #The code proceeds if no error is detected thus far
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
        
        res = bin_to_dec(binary) #We call our function
        print(f'Your binary number {num} returns the decimal number {res}')
        break #The while loop closes successfully

