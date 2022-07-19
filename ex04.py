string = 'Vitor'
tamString = len(string)
print(tamString)
inverter = string
for i in range(tamString - 1,0,-1):
    inverter += string[tamString - 1]
    print(inverter)
    tamString -= 1
print('===============')
print(inverter)