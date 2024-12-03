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
        titulo = "Sistema de Cadastramento de fornecedores - Lista de Empresas"
        self.titulo = titulo
        self.tela.title(titulo)
        self.tela.geometry("2400x307")
        
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
        self.cursor.execute("SELECT * FROM tb_empresa")
        tot_usuarios = self.cursor.fetchall()
        self.conn.close()

        self.tree = ttk.Treeview(self.tela, columns=("COD","CPF", "Nome_Empresarial", "Nome_Fantasia", "CNPJ", "Inscricao_Estadual", "Porte", "Desc_Atividades", "Pais", "Estado", "Bairro", "Municipio", "Logradouro", "Numero", "Complemento", "CEP", "Telefone", "Email"), show="headings")
        self.tree.heading("COD", text="COD")
        self.tree.column("COD", width=85)
        self.tree.heading("CPF", text="CPF Mandatário")
        self.tree.column("CPF", width=85)
        self.tree.heading("Nome_Empresarial", text="Nome Empresarial")
        self.tree.column("Nome_Empresarial", width=85)
        self.tree.heading("Nome_Fantasia", text="Nome Fantasia")
        self.tree.column("Nome_Fantasia", width=85)
        self.tree.heading("CNPJ", text="CNPJ")
        self.tree.column("CNPJ", width=85)
        self.tree.heading("Inscricao_Estadual", text="Inscrição Estadual")
        self.tree.column("Inscricao_Estadual", width=85)
        self.tree.heading("Porte", text="Porte")
        self.tree.column("Porte", width=85)
        self.tree.heading("Desc_Atividades", text="Descrição Atividades")
        self.tree.column("Desc_Atividades", width=85)
        self.tree.heading("Pais", text="País")
        self.tree.column("Pais", width=85)
        self.tree.heading("Estado", text="Estado")
        self.tree.column("Estado", width=85)
        self.tree.heading("Bairro", text="Bairro")
        self.tree.column("Bairro", width=85)
        self.tree.heading("Municipio", text="Município")
        self.tree.column("Municipio", width=85)
        self.tree.heading("Logradouro", text="Logradouro")
        self.tree.column("Logradouro", width=85)
        self.tree.heading("Numero", text="Número")
        self.tree.column("Numero", width=85)
        self.tree.heading("Complemento", text="Complemento")
        self.tree.column("Complemento", width=85)
        self.tree.heading("CEP", text="CEP")
        self.tree.column("CEP", width=85)
        self.tree.heading("Telefone", text="Telefone")
        self.tree.column("Telefone", width=85)
        self.tree.heading("Email", text="Email")
        self.tree.column("Email", width=85)

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
            self.cursor.execute("DELETE FROM tb_empresa WHERE cod_empresa=?",(idusuario,))
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
                self.cursor.execute("SELECT * FROM tb_empresa WHERE cod_empresa=?",(id_usuario,))
                usuario=self.cursor.fetchone()
                self.conn.close

                janela_nova=tk.Toplevel(self.tela)
                janela_nova.title(self.titulo+"alteracao")
                janela_nova.geometry("500x770")

                idlabel = tk.Label(janela_nova, text="codigo")
                idlabel.pack()
                idlabel2=tk.Label(janela_nova, text=id_usuario)
                idlabel2.pack()

                CPFlabel=tk.Label(janela_nova, text="CPF do Representante")
                CPFlabel.pack()
                CPFentry=tk.Entry(janela_nova)
                CPFentry.insert(0,usuario[1])
                CPFentry.pack()

                Nome_Empresariallabel=tk.Label(janela_nova, text="Nome_Empresarial")
                Nome_Empresariallabel.pack()
                Nome_Empresarialentry=tk.Entry(janela_nova)
                Nome_Empresarialentry.insert(0,usuario[2])
                Nome_Empresarialentry.pack()

                Nome_Fantasialabel=tk.Label(janela_nova, text="Nome_Fantasia")
                Nome_Fantasialabel.pack()
                Nome_Fantasiaentry=tk.Entry(janela_nova)
                Nome_Fantasiaentry.insert(0,usuario[3])
                Nome_Fantasiaentry.pack()

                CNPJlabel=tk.Label(janela_nova, text="CNPJ")
                CNPJlabel.pack()
                CNPJentry=tk.Entry(janela_nova)
                CNPJentry.insert(0,usuario[4])
                CNPJentry.pack()

                Inscricao_Estaduallabel=tk.Label(janela_nova, text="Inscricao_Estadual")
                Inscricao_Estaduallabel.pack()
                Inscricao_Estadualentry=tk.Entry(janela_nova)
                Inscricao_Estadualentry.insert(0,usuario[5])
                Inscricao_Estadualentry.pack()

                Portelabel=tk.Label(janela_nova, text="Porte")
                Portelabel.pack()
                Porteentry=tk.Entry(janela_nova)
                Porteentry.insert(0,usuario[6])
                Porteentry.pack()

                Desc_Atividadeslabel=tk.Label(janela_nova, text="Desc_Atividades")
                Desc_Atividadeslabel.pack()
                Desc_Atividadesentry=tk.Entry(janela_nova)
                Desc_Atividadesentry.insert(0,usuario[7])
                Desc_Atividadesentry.pack()

                Paislabel=tk.Label(janela_nova, text="Pais")
                Paislabel.pack()
                Paisentry=tk.Entry(janela_nova)
                Paisentry.insert(0,usuario[8])
                Paisentry.pack()

                Estadolabel=tk.Label(janela_nova, text="Estado")
                Estadolabel.pack()
                Estadoentry=tk.Entry(janela_nova)
                Estadoentry.insert(0,usuario[9])
                Estadoentry.pack()

                Bairrolabel=tk.Label(janela_nova, text="Bairro")
                Bairrolabel.pack()
                Bairroentry=tk.Entry(janela_nova)
                Bairroentry.insert(0,usuario[10])
                Bairroentry.pack()

                Municipiolabel=tk.Label(janela_nova, text="Municipio")
                Municipiolabel.pack()
                Municipioentry=tk.Entry(janela_nova)
                Municipioentry.insert(0,usuario[11])
                Municipioentry.pack()

                Logradourolabel=tk.Label(janela_nova, text="Logradouro")
                Logradourolabel.pack()
                Logradouroentry=tk.Entry(janela_nova)
                Logradouroentry.insert(0,usuario[12])
                Logradouroentry.pack()

                Numerolabel=tk.Label(janela_nova, text="Numero")
                Numerolabel.pack()
                Numeroentry=tk.Entry(janela_nova)
                Numeroentry.insert(0,usuario[13])
                Numeroentry.pack()

                Complementolabel=tk.Label(janela_nova, text="Complemento")
                Complementolabel.pack()
                Complementoentry=tk.Entry(janela_nova)
                Complementoentry.insert(0,usuario[14])
                Complementoentry.pack()

                CEPlabel=tk.Label(janela_nova, text="CEP")
                CEPlabel.pack()
                CEPentry=tk.Entry(janela_nova)
                CEPentry.insert(0,usuario[15])
                CEPentry.pack()

                Telefonelabel=tk.Label(janela_nova, text="Telefone")
                Telefonelabel.pack()
                Telefoneentry=tk.Entry(janela_nova)
                Telefoneentry.insert(0,usuario[16])
                Telefoneentry.pack()

                Emaillabel=tk.Label(janela_nova, text="Email")
                Emaillabel.pack()
                Emailentry=tk.Entry(janela_nova)
                Emailentry.insert(0,usuario[17])
                Emailentry.pack()

                def botao_gravar():
                    novoCPF = CPFentry.get()
                    novoNome_Empresarial = Nome_Empresarialentry.get()
                    novoNome_Fantasia=Nome_Fantasiaentry.get()
                    novoCNPJ=CNPJentry.get()
                    novoInscricao_Estadual=Inscricao_Estadualentry.get()
                    novoPorte=Porteentry.get()
                    novoDesc_Atividades=Desc_Atividadesentry.get()
                    novoPais=Paisentry.get()
                    novoEstado=Estadoentry.get()
                    novoBairro=Bairroentry.get()
                    novoMunicipio=Municipioentry.get()
                    novoLogradouro=Logradouroentry.get()
                    novoNumero=Numeroentry.get()
                    novoComplemento=Complementoentry.get()
                    novoCEP=CEPentry.get()
                    novoTelefone=Telefoneentry.get()
                    novoEmail=Emailentry.get()
                    self.conn=sqlite3.connect("siscadforn.db")
                    self.cursor=self.conn.cursor()
                    self.cursor.execute("UPDATE tb_empresa SET CPF=?, Nome_Empresarial=?, Nome_Fantasia=?, CNPJ=?, Inscricao_Estadual=?, Porte=?, Desc_Atividades=?, Pais=?, Estado=?, Bairro=?, Municipio=?, Logradouro=?, Numero=?, Complemento=?, CEP=?, Telefone=?, Email=? WHERE cod_empresa=?", (novoCPF, novoNome_Empresarial, novoNome_Fantasia, novoCNPJ, novoInscricao_Estadual, novoPorte, novoDesc_Atividades, novoPais, novoEstado, novoBairro, novoMunicipio, novoLogradouro, novoNumero, novoComplemento, novoCEP, novoTelefone, novoEmail, id_usuario))
                    self.conn.commit()
                    self.conn.close()

                    self.tree.item(item_selecionado, values=(id_usuario, novoCPF, novoNome_Empresarial, novoNome_Fantasia, novoCNPJ, novoInscricao_Estadual, novoPorte, novoDesc_Atividades, novoPais, novoEstado, novoBairro, novoMunicipio, novoLogradouro, novoNumero, novoComplemento, novoCEP, novoTelefone, novoEmail))
                gravar_button=tk.Button(janela_nova, text="Gravar", command=lambda:[botao_gravar()])
                gravar_button.pack()
                sair_button=tk.Button(janela_nova, text="Sair", command=janela_nova.destroy)
                sair_button.pack()


if __name__ == "__main__":
    tela = tk.Tk()
    lista = Listando(tela)
    tela.iconbitmap('brasao.ico')
    tela.mainloop()