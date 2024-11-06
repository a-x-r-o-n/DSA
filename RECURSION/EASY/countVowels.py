def countVowels(arr,count=0,vowels=['a','e','i','o','u','A','E','I','O','U']):
    if len(arr) == 0:
        return count
    if arr[0] in vowels:
        return countVowels(arr[1:],count+1)
    else:
        return countVowels(arr[1:],count)
    

print(countVowels("Aaron Joel"))