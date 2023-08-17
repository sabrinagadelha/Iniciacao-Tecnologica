p1 = input("Insira o primeiro ponto no formato x y: ").split()
p2 = input("Insira o segundo ponto no formato x y: ").split()
x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])
if x1 > x2:
    x_menor = x2
    y_menor = y2
else:
    x_menor = x1
    y_menor = y1
nome = input("Insira o endereço do arquivo: ")
arquivo = open(nome, "w")
arquivo.write("G21\n")
arquivo.write("G90\n")
arquivo.write("G28 X0 Y0\n")
arquivo.write(f"G92 X{x_menor} Y{y_menor}\n")
arquivo.write("M117 Mapeando...\n")
def gcode_file (x1, x2, y1, y2):
    tamanho_da_cama = 200
    comprimento_do_passo = 1
    numero_da_linha = 0
    tempo_de_espera = 200
    if x1 > x2:
        x_maior = x1
        y_maior = y1
        x_menor = x2
        y_menor = y2
    else:
        x_maior = x2
        y_maior = y2
        x_menor = x1
        y_menor = y1
    altura = y_maior - y_menor
    largura = x_maior - x_menor
    if altura < tamanho_da_cama:
        numero_de_linhas = int(altura/comprimento_do_passo) + 1
    else:
        numero_de_linhas = altura/comprimento_do_passo
    if largura < tamanho_da_cama:
        tamanho_da_linha = int(largura/comprimento_do_passo) + 1
    else:
        tamanho_da_linha = int(largura/comprimento_do_passo)
    while numero_da_linha < numero_de_linhas:
        numero_da_linha += 1
        if((numero_da_linha % 2) == 1):
            for i in range(tamanho_da_linha):
                x_menor += comprimento_do_passo
                print(f"G0 X{x_menor}", file = arquivo)
                print(f"G4 P{tempo_de_espera}", file = arquivo)
        else:
            for i in range(tamanho_da_linha):
                x_menor -= comprimento_do_passo
                print(f"G0 X{x_menor}", file = arquivo)
                print(f"G4 P{tempo_de_espera}", file = arquivo)
        y_menor += comprimento_do_passo
        print(f"G0 Y{y_menor}", file = arquivo)
        print(f"G4 P{tempo_de_espera}", file = arquivo)
gcode_file(x1, x2, y1, y2)
arquivo.write("M84 X Y")
arquivo.close()
