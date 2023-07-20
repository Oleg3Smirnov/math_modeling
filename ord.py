text = "Hello"

for symbol in text: 
    print(ord(symbol), end="; ") 
print() 

codes = [23, 43, 19]
symbols = ""

for code in codes: 
    symbols += chr(code) 

print(symbols) 
