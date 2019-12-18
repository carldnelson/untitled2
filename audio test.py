from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file("westside.mp3", format("mp3"))

#  play(song[1500:3000])
# play(song[:1500])
# play(song[1500:3000])
# play(song[1500:3000])

# initializing number
num = 2519

# printing number
print("The original number is " + str(num))

# using list comprehension
# to convert number to list of integers
digits = [int(x) for x in str(num)]

# printing result
print("The list from number is " + str(digits))

# Build a sentence from the list

# Thousands

Thousands = int(digits[-4])
print(Thousands)

# Hundreds
Hundreds = digits[-3]
print(Hundreds)

# Tens
Tens = 10 * digits[-2] + digits[-1]
print(Tens)

Sentence = ""

if Thousands != 0:
    Sentence += str(Thousands) + " Thousand"

if Hundreds != 0:
    Sentence += str(Hundreds) + " Hundred"


print(Sentence)
