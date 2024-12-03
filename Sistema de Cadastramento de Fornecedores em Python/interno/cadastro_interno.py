import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
import sqlite3

class Cad_interno:
    def lrepresentantes(self):
        self.tela.destroy()
        os.system("python interno/lista_representante.py")  

    def lempresas(self):
        self.tela.destroy()
        os.system("python interno/lista_empresa.py")  

    def cadinterno(self):
        self.tela.destroy()
        os.system("python interno/cadastro_interno.py")

    def linterno(self):
        self.tela.destroy()
        os.system("python interno/lista_interno.py") 

    def __init__(self, tela):
        self.tela=tela
        titulo="Sistema de Cadastramento de fornecedores - Cadastro de funcionario interno"
        self.titulo=titulo
        self.tela.title(titulo)
        self.tela.geometry("600x300")

        self.barraDeMenus = Menu(self.tela)
        self.menuFuncoes = Menu(self.barraDeMenus, tearoff=0)
        self.menuFuncoes.add_command(label="Lista Mandatários", command=self.lrepresentantes)
        self.menuFuncoes.add_command(label="Lista Empresas", command=self.lempresas)
        self.menuFuncoes.add_command(label="Cadastro Interno", command=self.cadinterno)
        self.menuFuncoes.add_command(label="Lista Interno", command=self.linterno)
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
    
        self.cpf_label=tk.Label(tela,text="cpf")
        self.cpf_label.pack()
        self.cpf_entry=tk.Entry(tela,width=30)
        self.cpf_entry.pack()

        self.nome_label=tk.Label(tela,text="nome")
        self.nome_label.pack()
        self.nome_entry=tk.Entry(tela,width=30)
        self.nome_entry.pack()

        self.email_label=tk.Label(tela,text="email")
        self.email_label.pack()
        self.email_entry=tk.Entry(tela,width=30)
        self.email_entry.pack()

        self.senha_label=tk.Label(tela,text="senha")
        self.senha_label.pack()
        self.senha_entry=tk.Entry(tela,width=30)
        self.senha_entry.pack()

        self.cadastrar_button = tk.Button(tela, text="Cadastrar representante", command=self.cadastrar)
        self.cadastrar_button.pack()

    def cadastrar(self):
        cpf=self.cpf_entry.get()
        nome=self.nome_entry.get()
        email=self.email_entry.get()
        senha=self.senha_entry.get()
        if (len(cpf.strip()))<=0 or (len(nome.strip())<=0) or (len(email.strip())<=0) or (len(senha.strip())<=0):
            messagebox.showinfo(self.titulo, "preencha todo os campos")
        else:
            self.cursor.execute("INSERT INTO tb_f_governo(cpf, nome, email, senha) VALUES(?, ?, ?, ?)", (cpf, nome, email, senha))

            self.conn.commit()
            floricultura=self.cursor.fetchone()
            if floricultura:
                messagebox.showerror("Aviso", "Erro!!")
            else:
                messagebox.showinfo("Aviso", "Sucesso!!")
                self.tela.destroy()
                os.system("python interno/menu_interno.py")
                
if __name__=="__main__":
    tela=tk.Tk()
    acesso=Cad_interno(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()