reverso = lambda s: s[::-1]
print(reverso("\n Python \n")) # nohtyP
print(reverso([1, 2, 3])) # [3, 2, 1]

nome = "Python"
print(len(nome)) # 6

cincoPrimeiros = lambda s: s[:5]
print(cincoPrimeiros(nome)) # Pytho

cincoPrimeiros_2 = lambda s: s[1:6]
print(cincoPrimeiros_2(nome)) # ython