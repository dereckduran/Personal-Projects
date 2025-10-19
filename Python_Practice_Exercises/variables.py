'''
rate = int(input("Please enter your rate:"))
hours = int(input("Please enter hours completed:"))

pay = rate * hours
print(f'Pay: {pay}')


celsius = float(input("Please enter your Celsius temperature: "))
print('Converting to Farenheit...')
farenheit = celsius*1.8+32
print(f'Farenheit: {farenheit}')
'''

def singleNumber(nums):
    hash = {}
    for i in nums:
        if i in hash:
            counter = hash[i] + 1
            hash[i] = counter
        else:
            counter = 1
            hash[i] = counter
    print(hash.items())

print(singleNumber([0,2,3,0]))
