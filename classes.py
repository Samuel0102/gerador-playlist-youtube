"""Esse módulo foi implementado para transferir músicas

Com uma playlist previamente criada no youtube
as músicas que estão na pasta musicas serão
adicionadas na playlist web

Autor: Samuel Pacheco Ferreira
"""


from selenium import webdriver
from time import sleep
from os import path, chdir, listdir



class DiretorioDeMusicas:
    """Classe que representa a pasta músicas

    Args:
        diretorio_musicas = pasta onde as músicas estão
    """


    def __init__(self):
        """método construtor

        """
        self.__diretorio_musicas = ""

    def acessar_diretorio_musicas(self):
        """Método responsável por encontrar a pasta músicas

        """
        diretorio_execucao = path.dirname(path.abspath(__file__))
        self.__diretorio_musicas = diretorio_execucao + "//musicas"

    def trocar_para_diretorio_musicas(self):
        """Método responsável por trocar o diretório atual

        Faz-se isso para varredura das músicas da pasta 

        """
        chdir(self.__diretorio_musicas)


class Google:
    """Classe que representa o navegador GOOGLE

    Args:
        navegador = armazena a janela do navegador para manipulações

    """


    def __init__(self):
        """método construtor
        """
        self.__navegador = None

    def acessar_google(self):
        """Método para abrir janela

        """
        self.__navegador = webdriver.Chrome()

    def get_google(self):
        """Método para retornar a janela para manipulação

        """
        return self.__navegador


class Usuario:
    """Classe que representa o usuário 

    Args:
        email_usuario (str)= email do usuário
        senha_usuario (str)= senha do usuário
        navegador ()= armazena a janela do navegador para manipulações
    """


    def __init__(self, email_usuario: str, senha_usuario: str, navegador: Google):
        """método construtor

        Args:
            email_usuario (str): email do usuário
            senha_usuario (str): senha do usuário
            navegador (Google): janela para manipulação
        """
        self.__email_usuario = email_usuario
        self.__senha_usuario = senha_usuario
        self.__navegador = navegador.get_google()

    def acessar_site_login(self):
        """Método para acessar login 

        É necessário logar em outra parte da web
        pois o GOOGLE barra login por testes automatizados

        """
        self.__navegador.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27")

    def logar(self):
        """Método para logar usuário por gmail

        """
        self.__navegador.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.__navegador.find_element_by_xpath('//input[@type="email"]').send_keys(self.__email_usuario)
        self.__navegador.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.__navegador.find_element_by_xpath('//input[@type="password"]').send_keys(self.__senha_usuario)
        self.__navegador.find_element_by_xpath('//*[@id="passwordNext"]').click()


class Playlist:
    """Classe que representa a playlist local e web

    Args:
        nome_playlist (str) = nome da playlist no youtube
        navegador (Google) = janela para manipulações
    """


    def __init__(self, nome_playlist: str, navegador: Google):
        """método construtor

        Args:
            nome_playlist (str): nome da playlist do youtube
            navegador (Google): janela para manipulações
        """
        self.__nome_playlist = nome_playlist
        self.__navegador = navegador.get_google()

    def acessar_youtube(self):
        """Método para acessar site youtube

        """
        self.__navegador.get('https://www.youtube.com/')

    def gerar_playlist_local(self):
        """Método para gerar playlist local 

        Varre a pasta música e adiciona os valores em lista

        Returns:
            list: lista contendo todas as músicas da pasta
        """
        playlist_local = list()
        for musicas in listdir():
            musica = musicas.replace(".mp3", "")
            playlist_local.append(musica)
        return playlist_local

    def pesquisar_musica(self, nome_musica: str):
        """Método para pesquisar música na barra de pesquisa

        Args:
            nome_musica (str): nome da música a pesquisar
        """
        self.__navegador.find_element_by_name("search_query").send_keys(nome_musica)
        self.__navegador.find_element_by_id("search-icon-legacy").click()
        sleep(2)
    
    def adicionar_musica_playlist_web(self):
        """Método para adicionar a música pesquisada na playlist
        
        """
        self.__navegador.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
        sleep(2)
        self.__navegador.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-button-renderer[2]/a').click()
        sleep(2)
        self.__navegador.find_element_by_xpath(f"//*[@id='checkbox-label']/yt-formatted-string[@title='{self.__nome_playlist}']").click()

