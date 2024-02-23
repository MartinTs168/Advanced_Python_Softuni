text = input()
symbols = sorted(set(text))
for current_symbol in symbols:
    print(f"{current_symbol}: {text.count(current_symbol)} time/s")
