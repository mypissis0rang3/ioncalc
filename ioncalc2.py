def calculator():

    print("\nI = g (Vm - Eion)\n")

    # Entrada
    I_input = input("Digite I ou ENTER: ")
    g_input = input("Digite g ou ENTER: ")
    Vm_input = input("Digite Vm ou ENTER: ")
    Eion_input = input("Escolha Eion (K, Na, Cl, Ca) ou ENTER: ").lower()

    # Conversão segura
    def to_float(x):
        return float(x.replace(",", ".")) if x else None

    I = to_float(I_input)
    g = to_float(g_input)
    Vm = to_float(Vm_input)

    ions = {
        "k": ("K+", -80),
        "na": ("Na+", 62),
        "cl": ("Cl-", -65),
        "ca": ("Ca2+", 123)
    }

    Eion = None
    if Eion_input in ions:
        nome, Eion = ions[Eion_input]

    # Mostrar equação com substituição parcial
    print(f"\n{I if I is not None else '[I]'} = "
          f"{g if g is not None else '[g]'} "
          f"({Vm if Vm is not None else '[Vm]'} - {Eion if Eion is not None else '[Eion]'})")

    # valores preenchidos
    valores = [I, g, Vm, Eion]
    preenchidos = sum(v is not None for v in valores)

    if preenchidos < 3:
        print("\nDados insuficientes (precisa de 3 valores)")
        return

    if preenchidos == 4:
        print("\nTodos os valores já foram fornecidos")
        return
    
    #calcs de vdd

    match (I is None, g is None, Vm is None, Eion is None):

        # Resolver I
        case (True, False, False, False):
            I = g * (Vm - Eion)
            print(f"\n{I} = {g} ({Vm} - {Eion})")

        # Resolver g
        case (False, True, False, False):
            if Vm == Eion:
                print("\nErro (Vm = Eion)")
                return
            g = I / (Vm - Eion)
            print(f"\n{I} = {g} ({Vm} - {Eion})")

        # Resolver Vm
        case (False, False, True, False):
            if g == 0:
                print("\nErro (g = 0)")
                return
            Vm = (I / g) + Eion
            print(f"\n{I} = {g} ({Vm} - {Eion})")

        # Resolver Eion
        case (False, False, False, True):
            if g == 0:
                print("\nErro (g = 0)")
                return
            Eion = Vm - (I / g)
            print(f"\n{I} = {g} ({Vm} - {Eion})")

        case _:
            print("\nErro inesperado")


def list_pr():
    print(""" \n PROPIEDADES
    Trata-se de uma calculadora de corrente iônica (aproximação fisiológica), assumindo:
    I : Quantidade de corrente elétrica
    g : Condutância
    Vm : Potencial de membrana
    Eion : Potencial de equilíbrio do íon
    V = Vm - Eion = Força impulsora iônica

    I = gV
    = g (Vm - Eion)

    Ek = -80 mV
    Ena = 62 mV
    Eca = 123 mV
    Ecl = -65 mV

    Adaptado do livro "Neurociências: Desvendando o Sistema Nervoso".      
    """)


def return_menu():
    while input("Digite 'menu' para retornar: ").lower() == "menu":
        print("Retornando ao menu")
        break

while True:
    print("\nMENU")
    print("1 - Calculadora")
    print("2 - Propriedades")
    print("3 - Sair")

    x = input("Insira 1, 2 ou 3: ")

    match x:
        case "1":
            calculator()
        case "2":
            list_pr()
        case "3":
            print("Saindo")
            break
        case _:
            print("Inválido")