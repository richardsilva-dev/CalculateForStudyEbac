from cycler import V
import re

text_oper = ["Potência", "Multiplicação", "Soma", "Divisão", "Subtração"]
str_oper = "P*+/-"
menu = [f"{str_oper[i]} - {text_oper[i]}" for i in range(0, 5)]
print("----CALCULADORA----")
print(
    f"[]Escolha alguma das opções abaixo \n{menu[0]}\n{menu[1]}\n{menu[2]}\n{menu[3]}"
)
tabela_calculate = "0P =,987*,654+,321/".split(",")
tabela_interface = [f"|{i[0]}|{i[1]}|{i[2]}|{i[3]}|" for i in tabela_calculate]
num = 0
while num == 0:
    num2 = 2
    print('example enter: "1 * 4"')
    for i in tabela_interface:
        print("_________")
        print(f"{i}")
    try:
        enter_number, enter_oper, enter_number2 = input("_________ > ").split()

        if enter_number.isnumeric() and enter_number2.isnumeric():
            if enter_oper in "Pp*+/-":
                list_nums = [(int(enter_number), int(enter_number2))]

                if enter_oper == "p" or enter_oper == "P":
                    func_oper1 = map(lambda lista: lista[0] ** lista[1], list_nums)
                    print(f" = {list(func_oper1)}")
                elif enter_oper == "*":
                    func_oper1 = map(lambda lista: lista[0] * lista[1], list_nums)
                    print(f" = {list(func_oper1)}")
                    while num2 == 2:
                        print("Continuar? s/n")
                        enter_sair = input().lower()
                        if enter_sair in "sn":
                            if enter_sair == "n":
                                num2 = 1
                                num = 1
                            else:
                                num2 = 1
                        else:
                            print("entrada inválida!")

                elif enter_oper == "+":
                    func_oper1 = map(lambda lista: lista[0] + lista[1], list_nums)
                    print(f" = {list(func_oper1)}")
                    while num2 == 2:
                        print("Continuar? s/n")
                        enter_sair = input().lower()
                        if enter_sair in "sn":
                            if enter_sair == "n":
                                num2 = 1
                                num = 1
                            else:
                                num2 = 1
                        else:
                            print("entrada inválida!")

                elif enter_oper == "/":
                    func_oper1 = map(lambda lista: lista[0] / lista[1], list_nums)
                    print(f" = {list(func_oper1)}")
                    while num2 == 2:
                        print("Continuar? s/n")
                        enter_sair = input().lower()
                        if enter_sair in "sn":
                            if enter_sair == "n":
                                num2 = 1
                                num = 1
                            else:
                                num2 = 1
                        else:
                            print("entrada inválida!")

                elif enter_oper == "-":
                    func_oper1 = map(lambda lista: lista[0] - lista[1], list_nums)
                    print(f" = {list(func_oper1)}")
                    while num2 == 2:
                        print("Continuar? s/n")
                        enter_sair = input().lower()
                        if enter_sair in "sn":
                            if enter_sair == "n":
                                num2 = 1
                                num = 1
                            else:
                                num2 = 1
                        else:
                            print("entrada inválida!")

            else:
                raise ValueError
        else:
            raise ValueError
    except (ZeroDivisionError, ValueError) as e:
        if e == ValueError:
            print("Ops ocorreu um erro , Tente novamente...")
