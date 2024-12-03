import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import *
import os

class Cad_representante:
    def cadempresa(self):
        self.tela.destroy()
        os.system("python usuario/cadastro_empresa.py")  

    def suporte(self):
        self.tela.destroy()
        os.system("python usuario/suporte.py")  

    def __init__(self, tela):
        self.tela=tela
        titulo="Sistema de Cadastramento de fornecedores - Cadastro de empresa"
        self.titulo=titulo
        self.tela.title(titulo)
        self.tela.geometry("500x710")

        self.barraDeMenus = Menu(self.tela)
        self.menuFuncoes = Menu(self.barraDeMenus, tearoff=0)
        self.menuFuncoes.add_command(label="Cadastro empresa", command=self.cadempresa)
        self.menuFuncoes.add_command(label="Suporte", command=self.suporte)
        self.menuFuncoes.add_separator()
        self.menuFuncoes.add_command(label="Sair", command=self.tela.quit)
        self.barraDeMenus.add_cascade(label="Funções", menu=self.menuFuncoes)
        self.tela.config(menu=self.barraDeMenus)

        

        self.conn=sqlite3.connect("siscadforn.db")
        self.cursor=self.conn.cursor()
        #self.cursor.execute("DROP TABLE IF EXISTS tb_empresa")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tb_empresa(
                cod_empresa INTEGER PRIMARY KEY,
                cpf TEXT,
                nome_empresarial TEXT,
                nome_fantasia TEXT,
                cnpj INTEGER,
                inscricao_estadual INTEGER,
                porte TEXT,
                desc_atividades TEXT,
                pais TEXT,
                estado TEXT,
                bairro TEXT,
                municipio TEXT,
                logradouro TEXT,
                numero INTEGER,
                complemento TEXT,
                cep TEXT,
                telefone INTEGER,
                email TEXT,
                FOREIGN KEY (cpf) REFERENCES tb_funcionario(cpf)
            )"""
        )

        self.cpf_label = tk.Label(tela, text="CPF do Representante")
        self.cpf_label.pack()
        self.cpf_entry = tk.Entry(tela, width=30)
        self.cpf_entry.pack()
    
        self.nome_empresarial_label=tk.Label(tela,text="nome_empresarial")
        self.nome_empresarial_label.pack()
        self.nome_empresarial_entry=tk.Entry(tela,width=30)
        self.nome_empresarial_entry.pack()

        self.nome_fantasia_label=tk.Label(tela,text="nome_fantasia")
        self.nome_fantasia_label.pack()
        self.nome_fantasia_entry=tk.Entry(tela,width=30)
        self.nome_fantasia_entry.pack()

        self.cnpj_label=tk.Label(tela,text="cnpj")
        self.cnpj_label.pack()
        self.cnpj_entry=tk.Entry(tela,width=30)
        self.cnpj_entry.pack()

        self.inscricao_estadual_label=tk.Label(tela,text="inscricao_estadual")
        self.inscricao_estadual_label.pack()
        self.inscricao_estadual_entry=tk.Entry(tela,width=30)
        self.inscricao_estadual_entry.pack()

        self.porte_label=tk.Label(tela,text="porte")
        self.porte_label.pack()
        self.porte_entry=tk.Entry(tela,width=30)
        self.porte_entry.pack()

        self.desc_atividades_label=tk.Label(tela,text="desc_atividades")
        self.desc_atividades_label.pack()
        self.desc_atividades_entry=tk.Entry(tela,width=30)
        self.desc_atividades_entry.pack()

        self.pais_label=tk.Label(tela,text="pais")
        self.pais_label.pack()
        self.pais_entry=tk.Entry(tela,width=30)
        self.pais_entry.pack()

        self.estado_label=tk.Label(tela,text="estado")
        self.estado_label.pack()
        self.estado_entry=tk.Entry(tela,width=30)
        self.estado_entry.pack()

        self.bairro_label=tk.Label(tela,text="bairro")
        self.bairro_label.pack()
        self.bairro_entry=tk.Entry(tela,width=30)
        self.bairro_entry.pack()

        self.municipio_label=tk.Label(tela,text="municipio")
        self.municipio_label.pack()
        self.municipio_entry=tk.Entry(tela,width=30)
        self.municipio_entry.pack()

        self.logradouro_label=tk.Label(tela,text="logradouro")
        self.logradouro_label.pack()
        self.logradouro_entry=tk.Entry(tela,width=30)
        self.logradouro_entry.pack()

        self.numero_label=tk.Label(tela,text="numero")
        self.numero_label.pack()
        self.numero_entry=tk.Entry(tela,width=30)
        self.numero_entry.pack()

        self.complemento_label=tk.Label(tela,text="complemento")
        self.complemento_label.pack()
        self.complemento_entry=tk.Entry(tela,width=30)
        self.complemento_entry.pack()

        self.cep_label=tk.Label(tela,text="cep")
        self.cep_label.pack()
        self.cep_entry=tk.Entry(tela,width=30)
        self.cep_entry.pack()

        self.telefone_label=tk.Label(tela,text="telefone")
        self.telefone_label.pack()
        self.telefone_entry=tk.Entry(tela,width=30)
        self.telefone_entry.pack()

        self.email_label=tk.Label(tela,text="email")
        self.email_label.pack()
        self.email_entry=tk.Entry(tela,width=30)
        self.email_entry.pack()

        self.cadastrar_button = tk.Button(tela, text="Cadastrar empresa", command=self.cadastrar)
        self.cadastrar_button.pack()

    def cadastrar(self):
        cpf = self.cpf_entry.get()
        nome_empresarial=self.nome_empresarial_entry.get()
        nome_fantasia=self.nome_fantasia_entry.get()
        cnpj=self.cnpj_entry.get()
        inscricao_estadual=self.inscricao_estadual_entry.get()
        porte=self.porte_entry.get()
        desc_atividades=self.desc_atividades_entry.get()
        pais=self.pais_entry.get()
        estado=self.estado_entry.get()
        bairro=self.bairro_entry.get()
        municipio=self.municipio_entry.get()
        logradouro=self.logradouro_entry.get()
        numero=self.numero_entry.get()
        complemento=self.complemento_entry.get()
        cep=self.cep_entry.get()
        telefone=self.telefone_entry.get()
        email=self.email_entry.get()
        if (len(cpf.strip())) <= 0 or (len(nome_empresarial.strip()))<=0 or (len(nome_fantasia.strip())<=0) or (len(cnpj.strip())<=0) or (len(inscricao_estadual.strip())<=0) or (len(porte.strip())<=0) or (len(desc_atividades.strip())<=0) or (len(pais.strip())<=0) or (len(estado.strip())<=0) or (len(bairro.strip())<=0) or (len(municipio.strip())<=0) or (len(logradouro.strip())<=0) or (len(numero.strip())<=0) or (len(complemento.strip())<=0) or (len(cep.strip())<=0) or (len(telefone.strip())<=0) or (len(email.strip())<=0):
            messagebox.showinfo(self.titulo, "preencha todo os campos")
        else:
            self.cursor.execute("INSERT INTO tb_empresa(cpf, nome_empresarial, nome_fantasia, cnpj, inscricao_estadual, porte, desc_atividades, pais, estado, bairro, municipio, logradouro, numero, complemento, cep, telefone, email) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (cpf, nome_empresarial, nome_fantasia, cnpj, inscricao_estadual, porte, desc_atividades, pais, estado, bairro, municipio, logradouro, numero, complemento, cep, telefone, email))

            self.conn.commit()
            floricultura=self.cursor.fetchone()
            if floricultura:
                messagebox.showerror("Aviso", "Erro!!")
            else:
                messagebox.showinfo("Aviso", "Sucesso!!")
                self.tela.destroy()
                os.system("python usuario/menu.py")
if __name__=="__main__":
    tela=tk.Tk()
    acesso=Cad_representante(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()