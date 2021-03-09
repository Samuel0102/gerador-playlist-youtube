from classes import DiretorioDeMusicas, Usuario, Playlist, Google
from os import path

# definindo  e acessando diretorio de musicas
diretorio = DiretorioDeMusicas()
diretorio.acessar_diretorio_musicas()
diretorio.trocar_para_diretorio_musicas()

# janela google
google = Google()
google.acessar_google()

# logando usuário no google
user_conta = input("Digite seu email: ")
user_senha = input("Digite sua senha: ")

usuario = Usuario(user_conta,user_senha, google)
usuario.acessar_site_login()
usuario.logar()

# abrindo playlist local  
playlist1 = Playlist("musicas", google)

# obter playlist local
playlist_local = playlist1.gerar_playlist_local()

# arquivo de erro para músicas que não foram adicionadas
arquivo = open(path.dirname(path.abspath(__file__))+"//musicas_nao_adicionadas.txt","a") 

# adicionar músicas na playlist youtube
for musica in playlist_local:
    playlist1.acessar_youtube()
    try:
        playlist1.pesquisar_musica(musica)
        playlist1.adicionar_musica_playlist_web()
    except:
        arquivo.write(musica+"\n")
        continue

arquivo.close()