from replit import clear
from art import logo
print(logo)
print("Bienvenido a la subasta")
pujas = {}
fin_subasta = False
def postor_mas_alto(recuento_pujas):
  puja_mas_alta = 0
  ganador = ""
  for pujador in recuento_pujas:
    monto_puja = recuento_pujas[pujador]
    if monto_puja > puja_mas_alta:
      puja_mas_alta = monto_puja
      ganador = pujador
  print(f"El ganador es {ganador} con una puja total de {puja_mas_alta} €")
  
while not fin_subasta:
  nombre = input("Por favor, introduce tu nombre. ")
  oferta = int(input("Bienvenido, cual es tu oferta?\n "))
  pujas[nombre] = oferta
  continuacion = input("Hay más pujadores ? Escribe si, o no ")
  if continuacion == "no":
    fin_subasta = True
    postor_mas_alto(pujas)
    print(pujas)
  elif continuacion == "si":
    clear()
    print(pujas)
    









  
    





