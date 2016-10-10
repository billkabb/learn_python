def func(str):
    str=str.replace("a","b")
    print str
sentence ="hallo"

############

sentence="hallo"

sentence1=sentence.encode("base64","strict")
print sentence1

#### kai decrypt
sentence2=sentence1.decode("base64","strict")
