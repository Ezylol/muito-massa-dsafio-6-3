n = int(input())

total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

for i in range(n):
  quantia, tipo = input().split()
  quantia = int(quantia)
  total_cobaias += quantia

  if tipo == 'R':
    total_ratos += quantia
  elif tipo == 'S':
    total_sapos += quantia
  elif tipo == 'C':
    total_coelhos += quantia

print(f"Total: {total_cobaias} cobaias")
print(f"Ratos: {total_ratos} ({total_ratos/total_cobaias*100:.2f}%)")
print(f"Sapos: {total_sapos} ({total_sapos/total_cobaias*100:.2f}%)")
print(f"Coelhos: {total_coelhos} ({total_coelhos/total_cobaias*100:.2f}%)")

print("Essas são as cobaias disponíveis! Obrigado por utilizar nosso sistema!")