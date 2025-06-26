# Gerador de senhas usando classes, funções e biblioteca gráfica TKinter
# PassDuck

import tkinter as tk
from random import choice
import pygame

class GeradorDeSenha:
    def __init__(self):
        self.caracteres_letras = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D',
                                'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H',
                                'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
                                'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P',
                                'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
                                'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X',
                                'y', 'Y', 'z', 'Z']
        self.caracteres_numeros = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.caracteres_especiais = ['!', '@', '#', '$', '%', '&']
        self.senha = ''
    
    def gerar_senha(self, tamanho, numeros=True, especiais=True):
        try:
            tamanho = int(tamanho)
            if tamanho <= 20 and tamanho > 4:
                caracteres_disponiveis = self.caracteres_letras.copy()
                if numeros:
                    caracteres_disponiveis.extend(self.caracteres_numeros.copy())
                if especiais:
                    caracteres_disponiveis.extend(self.caracteres_especiais.copy())
                
                self.senha = ''.join(choice(caracteres_disponiveis) for _ in range(tamanho))
                pygame.mixer.music.load('_internal/Quack_sound.mp3')
                pygame.mixer.music.play()
                return self.senha
            else:
                return f'Tamanho de senha inválida'
        except ValueError:
            return f'Digite um tamanho para a senha'
        
class Inteface(GeradorDeSenha):
    def __init__(self, janela):
        super().__init__()
        self.janela = janela
        self.janela.configure(bg='#e2f069')
        self.janela.title('PassDuck')
        self.janela.iconbitmap('_internal/PassDuck_ico.ico')
        self.janela.geometry('300x300')
        self.janela.resizable(False, False)
        
        # Texto da senha
        self.texto_senha = tk.Label(
            janela,
            text='---',
            bg='#e2f069',
            font=('Arial', 12)
        )
        self.texto_senha.pack(pady=25)
        
        # texto confirmação da cópia da senha
        self.confirmar_copia = tk.Label(
            janela,
            text='',
            bg='#e2f069'
        )
        self.confirmar_copia.pack()
        
        # Botão copiar senha
        self.botao_copiar_clipboard = tk.Button(
            janela,
            text='Copiar',
            justify='right',
            command=self.copiar_senha
        )
        self.botao_copiar_clipboard.pack(pady=5)
        
        # Botão de gerar a senha
        botao_gerador_senha = tk.Button(
            janela,
            text = 'Gerar Senha',
            justify = 'center',
            command= self.exibir_senha
        )
        botao_gerador_senha.pack(pady=10)
        
        # Texto explicação do tamanho da senha
        self.label_char = tk.Label(
            janela,
            bg='#e2f069',
            text='Tamanho da senha (mínimo 5; máximo 20):',
        )
        self.label_char.pack()
        
        # espaço para colocar a váriavel de char
        self.qnt_char = tk.Entry(
            janela,
            width=5,
            borderwidth=5,
            border=5
        )
        self.qnt_char.pack(pady=1)
        
        # checar se o usuário quer números
        self.check_num_var = tk.BooleanVar(value=True)
        self.numeros_check = tk.Checkbutton(
            janela,
            text='Números',
            bg="#e2f069",
            variable=self.check_num_var
        )
        self.numeros_check.pack(pady=5)
        
        # checar se o usuário quer caracteres especiais
        self.check_esp_char = tk.BooleanVar(value=True)
        self.especial_check = tk.Checkbutton(
            janela,
            text='Caracteres Especiais',
            bg='#e2f069',
            variable=self.check_esp_char
        )
        self.especial_check.pack(pady=5)
    
    # função de exibir a senha
    def exibir_senha(self):
        self.senha_gerada = self.gerar_senha(
            tamanho=self.qnt_char.get(),
            numeros=self.check_num_var.get(),
            especiais=self.check_esp_char.get()
            )
        self.texto_senha.config(text=self.senha_gerada)
    
    # função de copiar a senha
    def copiar_senha(self):
        if self.senha and self.senha_gerada != 'Tamanho de senha inválida' and self.senha_gerada != 'Digite um tamanho para a senha':
            janela.clipboard_clear()
            self.confirmar_copia.config(text='Senha copiada!', foreground='green')
            janela.clipboard_append(self.senha_gerada)
        else:
            pygame.mixer.music.load('_internal/fail.mp3')
            pygame.mixer.music.play()
            self.confirmar_copia.config(text='Nenhuma senha gerada...', foreground='red')
        
janela = tk.Tk()
interface_config = Inteface(janela)
pygame.mixer.init()
janela.mainloop()