import customtkinter
import sqlite3
from customtkinter import CTk



def abrir_janela_cadastro():
    janela_cadastro = customtkinter.CTk()
    janela_cadastro.geometry("400x200")
    janela_cadastro.title("Cadastro")
    janela_cadastro.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    gmail = customtkinter.CTkEntry(janela_cadastro, placeholder_text="usuario", width=200)
    gmail.pack(padx=10, pady=10)
    senha = customtkinter.CTkEntry(janela_cadastro, placeholder_text="senha", width=200)
    senha.pack(padx=10, pady=10)
    botao3 = customtkinter.CTkButton(janela_cadastro, text="Salvando Cadastro", command=lambda: abrir_cadastro(gmail, senha))
    botao3.pack(padx=10, pady=10)

    janela_cadastro.mainloop()

# Função para salvar o cadastro no banco de dados
def salvar_cadastro(email, senha):
    conn = sqlite3.connect('cadastros.db')
    c = conn.cursor()
    # Criação da tabela se ela não existir
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (email TEXT, senha TEXT)''')
    # Inserção dos dados do cadastro
    c.execute("INSERT INTO usuarios VALUES (?, ?)", (email, senha))
    conn.commit()
    conn.close()
    print("Cadastro salvo com sucesso!")

# Função para abrir o cadastro e chamar a função de salvar o cadastro
def abrir_cadastro(gmail, senha):
    email = gmail.get()
    senha_cadastro = senha.get()
    salvar_cadastro(email, senha_cadastro)

# Função para verificar o login no banco de dados
def verificar_login(gmail, senha):
    email = gmail.get()
    senha_login = senha.get()
    conn = sqlite3.connect('cadastros.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE email=? AND senha=?", (email, senha_login))
    resultado = c.fetchone()
    conn.close()
    return resultado

# Função para abrir a janela do menu após o login bem-sucedido
def abrir_janela_menu():
    janela_menu = customtkinter.CTk()
    janela_menu.geometry("1000x500")
    janela_menu.title("Painel")
    janela_menu.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    _menu = customtkinter.CTkLabel(janela_menu, text="Painel Principal", width=200)
    _menu.pack(padx=10, pady=10)

    janela_menu.mainloop()
    print("Login bem-sucedido! Abrindo janela de menu...")

# Função para clicar no botão de login
def clicar_botao_login(gmail, senha):
    resultado = verificar_login(gmail, senha)
    if resultado:
        abrir_janela_menu()
    else:
        print("Credenciais inválidas. Tente novamente.")

# Função para mostrar ou ocultar a senha
def password(senha):
    if senha.cget("show") == "":
        senha.configure(show="*")
    else:
        senha.configure(show="")

# Configuração da janela principal
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Cadastro / Login")
janela.resizable(False, False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Widgets da janela principal
texto = customtkinter.CTkLabel(janela, text="Login")
texto.pack(padx=10, pady=10)

gmail = customtkinter.CTkEntry(janela, placeholder_text="usuario", width=200)
gmail.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="senha", show="*", width=200)
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar Login")
checkbox.place(x=120, y=150)

botao1 = customtkinter.CTkButton(janela, text="Login", command=lambda: clicar_botao_login(gmail, senha))
botao1.place(x=100, y=200)

botao = customtkinter.CTkButton(janela, text="Cadastro", command=abrir_janela_cadastro)
botao.place(x=260, y=200)

botao_mostra_senha = customtkinter.CTkCheckBox(janela, text="Mostrar Senha", command=lambda: password(senha))
botao_mostra_senha.place(x=270, y=150)
# Inicialização da janela principal
janela.mainloop()
