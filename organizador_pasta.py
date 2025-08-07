# import os 
# from tkinter.filedialog import askdirectory

# caminho = askdirectory(title="selecione uma pasta")
# # print(caminho)
# lista_arquivos = os.listdir(caminho)
# print(lista_arquivos)

# locais = {
#     "imagens": [".png", "jpg",],
#     "arquivos":[".pdf",".zip",".docx"],
#     "jogos":[".iso"],
#     "instaladores": [".exe"],
# }

# for arquivo in lista_arquivos:
#     # 01. arquivo.pdf
#     nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
#     for pasta in locais:
#         if extensao in locais [pasta]:
#             if not os.path.exists(f"{caminho}/{pasta}"): #se n existe a pasta 
#                 os.mkdir(f"{caminho}/{pasta}") #cria a pasta
#             os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

import os 
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)
print(f"Pasta selecionada: {caminho}")
print("Arquivos encontrados:", lista_arquivos)

locais = {
    "imagens": [".png", ".jpg"],
    "arquivos": [".pdf", ".zip", ".docx",".doc"],
    "jogos": [".iso"],
    "instaladores": [".exe"],
    "audios": [".mp4",".wav"],
    "python" : [".py"],
}

for arquivo in lista_arquivos:
    origem = os.path.join(caminho, arquivo)

    # Ignora diretórios
    if os.path.isdir(origem):
        print(f"Ignorado (é uma pasta): {arquivo}")
        continue

    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    if extensao == "":
        print(f"Ignorado (sem extensão): {arquivo}")
        continue

    movido = False
    for pasta in locais:
        if extensao in locais[pasta]:
            destino_pasta = os.path.join(caminho, pasta)

            # Cria a pasta, se necessário
            if not os.path.exists(destino_pasta):
                os.mkdir(destino_pasta)
                print(f"Criada pasta: {destino_pasta}")

            destino_arquivo = os.path.join(destino_pasta, arquivo)

            try:
                os.rename(origem, destino_arquivo)
                print(f"Movido: {arquivo} → {pasta}")
                movido = True
            except Exception as e:
                print(f"Erro ao mover {arquivo}: {e}")
            break

    if not movido:
        print(f"Nenhuma correspondência para: {arquivo}")


