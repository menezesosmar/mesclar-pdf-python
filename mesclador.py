# "pip install pypdf2" biblioteca que manipula pdfs.
import PyPDF2 as pypdf 
# biblioteca nativa do python que permite manipular e ler arquivos de uma pasta local.
import os 

# função que irá mesclar os arquivos.
merger = pypdf.PdfMerger()
# "os" foi chamado para listar os arquivos contidos na minha pasta "arquivos".
lista_arquivos = os.listdir("arquivos")
# sort() ordena alfabeticamente os arquivos.
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
  # verificar se todos os arquivos são pdfs antes de mesclar.
  if '.pdf' in arquivo:
      # o merger irá adicionar o arquivo pdf dentro da pasta arquivos/.
      merger.append(f'arquivos/{arquivo}')

# para salvar, o merger cria o arquivo mesclado.
merger.write('PDF_final2.pdf')



