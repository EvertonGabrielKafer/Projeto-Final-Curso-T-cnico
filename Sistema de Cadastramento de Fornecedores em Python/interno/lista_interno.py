import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import sqlite3
from tkinter import *
import os


class Listando:
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
        self.tela = tela
        titulo = "Sistema de Cadastramento de fornecedores - Lista funcionarios internos"
        self.titulo = titulo
        self.tela.title(titulo)
        self.tela.geometry("1010x307")
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

        self.conn = sqlite3.connect("siscadforn.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM tb_f_governo")
        tot_usuarios = self.cursor.fetchall()
        self.conn.close()

        self.tree = ttk.Treeview(self.tela, columns=("COD", "CPF", "Nome", "Email", "Senha"), show="headings")
        self.tree.heading("COD", text="COD")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Senha", text="Senha")

        for cont_usuario in tot_usuarios:
            self.tree.insert("", tk.END, values=cont_usuario)

        self.tree.pack()

        self.excluir_botao = tk.Button(tela, text="Excluir", command=self.excluir, width=15, height=2)
        self.excluir_botao.pack()
        self.alterar_botao=tk.Button(tela,text="Alterar", command=self.alterar, width=15, height=2)
        self.alterar_botao.pack()
    def excluir(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            messagebox.showinfo(self.titulo, "Selecione uma linha")
        else:
            self.conn=sqlite3.connect("siscadforn.db")
            self.cursor = self.conn.cursor()
            idusuario=self.tree.item(item_selecionado,"values")[0]
            self.cursor.execute("DELETE FROM tb_f_governo WHERE cod_f_governo=?",(idusuario))
            self.conn.commit()
            self.conn.close()
            self.tree.delete(item_selecionado)
            messagebox.showinfo(self.titulo, "Escluido!")

            
    def alterar(self):
            item_selecionado=self.tree.selection()
            if not item_selecionado:
                messagebox.showinfo(self.titulo,"Selecione uma linha")
            else:
                item_selecionado=self.tree.selection()[0]
                id_usuario = self.tree.item(item_selecionado,"values")[0]
                self.conn=sqlite3.connect("siscadforn.db")
                self.cursor=self.conn.cursor()
                self.cursor.execute("SELECT * FROM tb_f_governo WHERE cod_f_governo=?",(id_usuario))
                usuario=self.cursor.fetchone()
                self.conn.close

                janela_nova=tk.Toplevel(self.tela)
                janela_nova.title(self.titulo+"alteracao")
                janela_nova.geometry("600x300")

                idlabel = tk.Label(janela_nova, text="codigo")
                idlabel.pack()
                idlabel2=tk.Label(janela_nova, text=id_usuario)
                idlabel2.pack()

                cpflabel=tk.Label(janela_nova, text="cpf")
                cpflabel.pack()
                cpfentry=tk.Entry(janela_nova)
                cpfentry.insert(0,usuario[1])
                cpfentry.pack()

                nomelabel=tk.Label(janela_nova, text="nome")
                nomelabel.pack()
                nomeentry=tk.Entry(janela_nova)
                nomeentry.insert(0,usuario[2])
                nomeentry.pack()

                emaillabel=tk.Label(janela_nova, text="email")
                emaillabel.pack()
                emailentry=tk.Entry(janela_nova)
                emailentry.insert(0,usuario[3])
                emailentry.pack()

                senhalabel=tk.Label(janela_nova, text="senha")
                senhalabel.pack()
                senhaentry=tk.Entry(janela_nova)
                senhaentry.insert(0,usuario[4])
                senhaentry.pack()

                def botao_gravar():
                    novocpf = cpfentry.get()
                    novonome=nomeentry.get()
                    novoemail=emailentry.get()
                    novosenha=senhaentry.get()
                    self.conn=sqlite3.connect("siscadforn.db")
                    self.cursor=self.conn.cursor()
                    self.cursor.execute("UPDATE tb_f_governo SET cpf=?, nome=?, email=?, senha=? WHERE cod_f_governo=?", (novocpf, novonome, novoemail, novosenha, id_usuario))
                    self.conn.commit()
                    self.conn.close()

                    self.tree.item(item_selecionado, values=(id_usuario, novocpf, novonome, novoemail, novosenha))
                gravar_button=tk.Button(janela_nova, text="Gravar", command=lambda:[botao_gravar()])
                gravar_button.pack()
                sair_button=tk.Button(janela_nova, text="Sair", command=janela_nova.destroy)
                sair_button.pack()


if __name__ == "__main__":
    tela = tk.Tk()
    lista = Listando(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()