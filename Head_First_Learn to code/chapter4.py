#Lists
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54]
score = scores[3]
print('Solution #3 produced', score, 'bubbles.'  )

smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']
print(smoothies)
favorite = smoothies[2]
print(favorite)
smoothies[3] = 'tropical'
print(smoothies)
#length of smoothies
length = len(smoothies)
print(length)
#select last one
last = smoothies[length-1]
print(last)
last = smoothies[-1]
print(last)
second_last = smoothies[-2]
print(second_last)
third_last = smoothies[-3]
print(third_last)



eighties = ['', 'duran duran', 'B-52s', 'muse']
newwave = ['flock of seagulls', 'postal service']
remember = eighties[1]
eighties[1] = 'culture club'
band = newwave[0]
eighties[3] = band
eighties[0] = eighties[2]
eighties[2] = remember
print(eighties)



charactors = ['t', 'a', 'c', 'o']
output = ''
length = len(charactors)
i = 0
while(i < length):
    output = output + charactors[i]
    i = i + 1
length = length * -1
i = -2
while(i >= length):
    output = output + charactors[i]
    i = i - 1
print(output)



charactors = ['w', 'a', 's', 'i', 't', 'a', 'r']
output = ''
length = len(charactors)
i = 0
while(i < length):
    output = output + charactors[i]
    i = i + 1
length = length * -1
i = -2
while(i >= length):
    output = output + charactors[i]
    i = i - 1
print(output)



charactors = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c']
output = ''
length = len(charactors)
i = 0
while(i < length):
    output = output + charactors[i]
    i = i + 1
length = length * -1
i = -2
while(i >= length):
    output = output + charactors[i]
    i = i - 1
print(output)