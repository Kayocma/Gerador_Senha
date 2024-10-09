import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

def gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ''

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres: # Se nenhum tipo de caractere foi selecionado
        raise ValueError('Nenhum tipo de caractere foi selecionado')
    
    # Garantir que a senha tenha pelo menos um caractere de cada tipo
    senha = []
    if incluir_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if incluir_minusculas:
        senha.append(random.choice(string.ascii_lowercase))
    if incluir_numeros:
        senha.append(random.choice(string.digits))
    if incluir_simbolos:
        senha.append(random.choice(string.punctuation))

    # Completar o restante da senha
    for i in range(tamanho - len(senha)):
        senha.append(random.choice(caracteres))

    # Embaralhar a senha
    random.shuffle(senha)
    return ''.join(senha)

def salvar_senha(senha):
    with open('senhas.txt', 'a') as arquivo:
        arquivo.write(senha + '\n')

def gerar_senha_interface():
    try:
        tamanho = int(entry_tamanho.get())
        incluir_maiusculas = var_maiusculas.get()
        incluir_minusculas = var_minusculas.get()
        incluir_numeros = var_numeros.get()
        incluir_simbolos = var_simbolos.get()

        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def copiar_senha():
    senha = entry_senha.get()
    pyperclip.copy(senha)
    messagebox.showinfo("Informação", "Senha copiada com sucesso!")

def salvar_senha_interface():
    senha = entry_senha.get()
    salvar_senha(senha)
    messagebox.showinfo("Informação", "Senha salva com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

tk.Label(root, text="Tamanho da senha:").grid(row=0, column=0, padx=10, pady=10)
entry_tamanho = tk.Entry(root)
entry_tamanho.grid(row=0, column=1, padx=10, pady=10)

var_maiusculas = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=var_maiusculas).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

var_minusculas = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir letras minúsculas", variable=var_minusculas).grid(row=2, column=0, columnspan=2, padx=10, pady=5)

var_numeros = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir números", variable=var_numeros).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

var_simbolos = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir símbolos", variable=var_simbolos).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

tk.Button(root, text="Gerar Senha", command=gerar_senha_interface).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Senha gerada:").grid(row=6, column=0, padx=10, pady=10)
entry_senha = tk.Entry(root, width=50)
entry_senha.grid(row=6, column=1, padx=10, pady=10)

tk.Button(root, text="Copiar", command=copiar_senha).grid(row=7, column=0, padx=10, pady=10)
tk.Button(root, text="Salvar", command=salvar_senha_interface).grid(row=7, column=1, padx=10, pady=10)

root.mainloop()