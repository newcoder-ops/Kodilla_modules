def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

items = ["cola", "burger", "fries"]
text = shopping(items, 'card', 'small local shop')
print(text)
print("_____________________________")
print("Pokażę wszystko, co wpiszesz!")
text = input()
print("Oto Twój tekst: ***%s***" % text)
text = input("Wpisz swój tekst:")


items_text = "cola,whiskey,lód"
items = items_text.split(',')
print(type(items))
print(len(items))

