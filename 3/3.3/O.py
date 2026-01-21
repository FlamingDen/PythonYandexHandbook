text = "Мама мыла раму!"
print({char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()})
