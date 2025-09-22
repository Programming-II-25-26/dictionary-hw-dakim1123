#Check if given key already exists in dictionary

mydict = {
    "Monday" : 2,
    "Tuesday" : 2,
    "Wednesday" : 1,
    "Thursday" : 2, 
    "Friday" : 2
}

def lunchcheck(dict, key):
    if key in dict:
        return True
    return False

print(lunchcheck(mydict, "Monday"))
print(lunchcheck(mydict, "Saturday"))


#Number dictionary

nums = {}

try:
    inputnum = int(input("How many sets of numbers do you want? "))
except ValueError:
    print("invalid input")

for i in range(inputnum):
    nums[i+1] = (i+1)*(i+1)

print(nums)


#duplicate letters in a word

dict = {}

wordinput = str(input("Type in a word: "))
listword = list(wordinput)

for letter in listword:
    if letter not in dict:
        dict[letter] = 1
    elif letter in dict:
        dict[letter] += 1

for letter in listword:
    if dict[letter] < 2:
        del dict[letter]

print(dict)


#Extract mentioned keys

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

new_dict = {}

extract_input = input("What keys should be extracted? ")
extract_key = extract_input.split()

for keys in extract_key:
    if keys in sample_dict:
        new_dict[keys] = sample_dict[keys]

print(new_dict)