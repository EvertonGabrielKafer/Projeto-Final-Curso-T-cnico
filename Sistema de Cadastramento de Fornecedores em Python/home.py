import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os

class Home:

    def __init__(self, tela):
        self.tela=tela
        titulo="Sistema de Cadastramento de fornecedores - Home"
        self.titulo=titulo
        self.tela.title(titulo)
        self.tela.geometry("500x200")
        
        self.explicacao_label = tk.Label(
            tela, 
            text="Sistema de cadastramento de fornecedores",
            wraplength=400,
            
        )
        self.explicacao_label.pack(pady=10)

        self.explicacao_label = tk.Label(
            tela, 
            text="O cadastramento de fornecedor deve ser iniciado por meio da opção Cadastro. "
                 "O processo de cadastramento refere-se ao preenchimento de formulários eletrônicos apropriados.",
            wraplength=400,
        )
        self.explicacao_label.pack(pady=10)

        self.login_button = tk.Button(tela, text="Login", command=self.login)
        self.login_button.pack()
        self.cadastro_button = tk.Button(tela, text="Cadastro", command=self.cadastro)
        self.cadastro_button.pack()
        self.interno_button = tk.Button(tela, text="Acesso Interno", command=self.interno)
        self.interno_button.pack()

    def login(self):
                self.tela.destroy()
                os.system("python usuario/acesso.py")
                

    def cadastro(self):
                messagebox.showinfo("Aviso", "Preencha o cadastro a seguir com todas as informações necessárias.")
                self.tela.destroy()
                os.system("python usuario/cadastro_representante.py")

    def interno(self):
                self.tela.destroy()
                os.system("python interno/acesso_interno.py")
                

if __name__ == "__main__":
    tela = tk.Tk()
    Home = Home(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()