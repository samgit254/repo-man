# Repo-Man 

## Binary to Decimal Conversion 

So far so good with the binary number converter. Hopefully it is different from what you are used to seeing. Your decimal number will be converted to a list first then the code works with the list elements, popping the first element with each run until the list is empty and the loop breaks succefully. 

The error handling also won't allow a user to input any number that is not a binary number and once it starts running it only terminates when the input is the correct type. 

Alternatively, you can write your code as so.

    class NonBinaryError(Exception):
         pass
         
    def bin_to_dec(binary):
        while binary:
          bin_len = len(binary)
          dec_num = 0
          for i in range(bin_len):
              x = 2**i
              if binary[-1]:
                  dec_num += x
              else:
                  dec_num += 0
              del binary[-1]   
    return dec_num
    
    while True:
    try:
        num = int(input('Type in your binary number: '))
        binary = [int(x) for x in str(num)]
        for x in binary:
            if x > 1:
                raise NonBinaryError
        res = bin_to_dec(binary)
        print(f'Your binary number {num} returns the decimal number {res}')
        break
    except NonBinaryError:
        print('The number is non-binary, input an actual binary number.')
    except ValueError:
        print('Invalid input, type in your binary number')
 
