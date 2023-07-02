Entrada = input("Insira seu tipo sanguíneo [A/B/O]: ").upper()

if Entrada == "O":
    print("O seu sangue é compatível com A, B e AB")
if Entrada == "B":
    print("Seu sangue é compatível com B e AB")
elif Entrada == "A":
    print("O tipo de sangue A é compatível com A e AB")
