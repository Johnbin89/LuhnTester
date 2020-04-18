   
def luhn_sum(string):
    """
    Creates a list r, with the digits of the number(string type) from last to first digit. \n
    Calculates the sum in 0,2,4.. indexes \n
    Calculates the sum in 1,3,5... indexes with every number above 9 converted to the sum of its digits \n
    Adds two sums and returns total mod 10
    """
    r = [int(ch) for ch in string][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10


def find_check_digit(string):
    return (10 - luhn_sum(string + '0')) % 10



def verify_number(string):
    return (luhn_sum(string) == 0)



'''
def generate(string):
    return "%s%s" % (string, find_check_digit(string))

string = '79927398714'
print('Check Digit            :', find_check_digit(string))
print('Input Card Number      :', string, 'is', verify_number(string))
print('Number and Check Digit :', generate(string))
luhn_sum('79927398710')
'''