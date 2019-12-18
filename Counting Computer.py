# Python3 program to convert a list
# of integers into a single integer

# Define the dictionary for audio files
audio = {
    1: 'one.wav', 2: 'two.wave', 3: 'three.wav', 4: 'four.wave', 5: 'five.wav',
    6: 'six.wave', 7: 'seven.wav', 8: 'eight.wave', 9: 'nine.wav', 10: 'ten.wave',
    11: 'eleven.wav', 12: 'twelve.wave', 13: 'thirteen.wav', 14: 'fourteen.wave', 15: 'fifteen.wav',
    16: 'sixteen.wave', 17: 'seventeen.wav', 18: 'eighteen.wave', 19: 'nineteen.wav',
    20: 'twenty.wave', 30: 'thirty.wav', 40: 'fourty.wave', 50: 'fifty.wav', 60: 'sixty.wave', 70: 'seventy.wav',
    80: 'eighty.wave', 90: 'ninety.wav',
    100: 'hundred.wave', 1000: 'thousand.wav', 1000000: 'million.wave', 1000000000: 'billion.wav',
    1000000000000: 'trillion.wave'
}

# added to git

def convert(list):
    # Convert a list of integers to a string list
    # then join the list using join()
    if list:  # List is not empty
        res = int("".join(map(str, list)))
    else:
        res = 0
    return res


# Given a number, return the hundred place holder and the tens units
def split(number):
    # should add in a check that number is less than 1000
    # otherwise return an error
    if number < 100:  # is number less than 100?
        hundred = number // 100
        print(hundred)
        tens = number - (hundred * 100)
        print(tens)
    else:
        hundred = 0
        tens = number - (hundred * 100)
    return (hundred, tens)


number = 733056456343
dnumber = [int(x) for x in str(number)]

# convert our number to a list of digits that we can split up

hundreds = convert(dnumber[-3:])
print("hundreds", hundreds)
thousands = convert(dnumber[-6:-3])
print("thousands", thousands)
millions = convert(dnumber[-9:-6])
print('millions', millions)
billions = convert(dnumber[-12:-9])
print('billions', billions)

audio = ""
if split(billions)[0] != 0:
    audio += str(split(billions)[0]) + ' hundred ' + str(split(billions)[1]) + ' billion '
else:
    audio += str(split(billions)[1])

print('audio would say', audio)
