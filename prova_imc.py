peso=float(input("digite a sua altura:"))
altura=float(input("digite o seu peso:"))
imc= peso/ (altura**2)

if imc>30.0:
    print("cuidado com a saude")
if imc>25.0:
    print("esta bom!")
else:
    print("tudo ok!")