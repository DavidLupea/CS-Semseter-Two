#David Lupea
#INTROCS2 pd05
#HW 06 -- PairingMagic
#2018-2-11

def magicPair(m, n):
    tens_and_ones_of_m = m % 100
    tens_and_ones_of_n = n % 100

    ones_m = tens_and_ones_of_m % 10
    ones_n = tens_and_ones_of_n % 10
    ten_m = (tens_and_ones_of_m - ones_m) / 10
    ten_n = (tens_and_ones_of_n - ones_n) / 10

    if ((ones_m == ones_n) or (ten_m == ten_n)) and (ones_m + ones_n == ten_m + ten_n):
        return True 
    elif ((ones_m == ten_n) or (ten_m == ones_n)) and (ones_m + ten_n == ten_m + ones_n):
        return True  
    else:
        return False
        
