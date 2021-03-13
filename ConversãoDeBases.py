print("\033[31;40m-=-"*54)
header = ("Conversor de bases")
print(header.center(160))
print("\033[31;40m-=-"*54)

num = int(input("Escolha um numero: "))
print("""Escolha uma opção: 
[1] Binario
[2] Octal
[3] Exadecimal""")
opcao = int(input("Digite a opção: "))

if (opcao == 1):
    print("{} convertido para binario é de {}".format(num, bin(num)[2:]))
elif (opcao == 2):
    print("{} convertido para Octal é de {}".format(num, oct(num)[2:]))
elif (opcao == 3):
    print("{} convertido para Hexadecimal é de {}".format(num, hex(num)[2:]))
else:
    print("Opcão invalida, tente novamente.")