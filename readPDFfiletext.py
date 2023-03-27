import slate3k as slate

text = slate.PDF(open('./PYTHON cheat sheet.pdf', 'rb')).text()
print(text)