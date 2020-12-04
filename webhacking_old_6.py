import base64

text = "admin".encode('utf-8')
text2 = "nimda".encode('utf-8')


def stringTobase64(s):
    return base64.b64encode(s)

def base64Tostring(s):
    return base64.b64decode(s).decode('utf-8')

for n in range(20):
    text = stringTobase64(text)
    text2 = stringTobase64(text2)

text = text.decode('utf-8')
text2 = text2.decode('utf-8')

text = text.replace('1','!')
text = text.replace("2","@")
text = text.replace("3","$")
text = text.replace("4","^")
text = text.replace("5","&")
text = text.replace("6","*")
text = text.replace("7","(")
text = text.replace("8",")")

text2 = text2.replace("1","!")
text2 = text2.replace("2","@")
text2 = text2.replace("3","$")
text2 = text2.replace("4","^")
text2 = text2.replace("5","&")
text2 = text2.replace("6","*")
text2 = text2.replace("7","(")
text2 = text2.replace("8",")")

print(text)
print("----------------------------")
print(text2)