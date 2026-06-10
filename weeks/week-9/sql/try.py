data = {'unit': '8200', 'classification': 'secret', 'content': 'Encrypted signal intercepted on frequency 312.', 'source': 'sigint'}

a = [f"{kay}= %s" for kay in data.keys()]

b = list(data.values())
print(b)


