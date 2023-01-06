def coding(word):
    copy_word=word
    if(len(word)>=3):
        ch=word[0]
        copy_word=copy_word.replace(ch,'',1)
        copy_word+=ch
        random_string1="!%&"
        random_string2=":@#"
        copy_word=random_string1+copy_word+random_string2
        return copy_word
    else:
        copy_word=copy_word[::-1] #reverse the string   
        return copy_word 
def decoding(word):
    copy_word=word
    if(len(word)>=3):
        str1=copy_word[0]+copy_word[1]+copy_word[2]
        str2=word[len(copy_word)-3]+word[len(copy_word)-2]+word[len(copy_word)-1]
        copy_word=copy_word.replace(str1,"")
        copy_word=copy_word.replace(str2,"")
        countNum=len(copy_word)-1
        ch=copy_word[countNum:]
        copy_word=copy_word.replace(ch,'')
        # ch=copy_word[len(copy_word)-1]
        copy_word=ch+copy_word
        return copy_word
    else:
        copy_word=copy_word[::-1] #reverse the string    
        return copy_word


word=input("Enter a word to convert it to a code! ")
print(f"Encoded form of {word} is ->",coding(word))
x=coding(word)
print(f"Decoded form of {coding(word)} is ->",decoding(x))