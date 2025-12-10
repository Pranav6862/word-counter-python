

def count_words(input_string):
    count_char =len(input_string)
    
    vowels="aeiouAEIOU"
    vowel_count=0

    for ch in input_string:
        if ch in vowels:
            vowel_count +=1

    word_count =len(input_string.split())
    return count_char, vowel_count, word_count
    

input_string=input("Enter a string:")
chars, vowels, words = count_words(input_string)

print(f"Number of character: {chars}")
print(f"Number of vowels: {vowels}")
print(f"Number of words: {words}")

# for char in str:
#     if char.isalpha():
#         count_char1 += 1
# print(count_char1)
