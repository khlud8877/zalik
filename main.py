f1 = open("file1.txt", 'r+')
txt = f1.read()
text = txt.split()
print(text)
w1 = input("Введіть перше слово:")
w2 = input("Введіть друге слово:")
if w1 in text:
    for n, i in enumerate(text):
        if i == w1:
            text[n] = w2
    print(text)
else:
    print("Немає такого слова")
text = str(text)
f1.close()
f1 = open("file1.txt", "w")
f1.write(text)
f1.close()