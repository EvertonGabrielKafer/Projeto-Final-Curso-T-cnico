import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
import sqlite3

class LoginSystem:

    def voltar(self):
        self.tela.destroy()
        os.system("python home.py") 
        
    def __init__(self, tela):
        self.tela=tela
        titulo="Sistema de Cadastramento de fornecedores - Login interno"
        self.titulo=titulo
        self.tela.title(titulo)
        self.tela.geometry("500x200")

        self.barraDeMenus = Menu(self.tela)
        self.menuFuncoes = Menu(self.barraDeMenus, tearoff=0)
        self.menuFuncoes.add_command(label="Voltar", command=self.voltar)
        self.menuFuncoes.add_separator()
        self.menuFuncoes.add_command(label="Sair", command=self.tela.quit)
        self.barraDeMenus.add_cascade(label="Funções", menu=self.menuFuncoes)
        self.tela.config(menu=self.barraDeMenus)

        self.conn=sqlite3.connect("siscadforn.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS tb_f_governo(
                    cod_f_governo INTEGER PRIMARY KEY,
                    cpf INTEGER,
                    nome TEXT,
                    email TEXT,
                    senha TEXT
                )"""
        )
    
        self.email_label = tk.Label(tela, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(tela, width=30)
        self.email_entry.pack()
        self.senha_label = tk.Label(tela, text="Senha:")
        self.senha_label.pack()
        self.senha_entry = tk.Entry(tela, width=30, show="*")
        self.senha_entry.pack()
        self.login_button = tk.Button(tela, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        #nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        if len(email.strip()) <=0 and len(senha.strip()) <= 0:
            messagebox.showinfo("Sistema de login", "Campos nao preenchidos")
        else:
            self.cursor.execute("SELECT * FROM tb_f_governo WHERE email=? AND senha=?", (email,senha))
            usuario = self.cursor.fetchone()
            if usuario:
                messagebox.showinfo("Sistema de login", "Bem vindo")
                self.tela.destroy()
                os.system("python interno/menu_interno.py")
            else:
                messagebox.showerror("Sistema de login", "Email ou senha incorretos")

if __name__ == "__main__":
    tela = tk.Tk()
    LoginSystem = LoginSystem(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()