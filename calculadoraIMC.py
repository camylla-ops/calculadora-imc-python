import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
root = tk.Tk()
root.title("🍑 Calculadora de IMC 🍬")
root.geometry("320x300")
root.configure(bg="#FFE6F2")  # Fundo rosa claro

# Fonte fofa
fonte_titulo = ("Comic Sans MS", 12, "bold")  
fonte_normal = ("Comic Sans MS", 10)

# Criar rótulos e caixas de entrada com estilo
tk.Label(root, text="✏️ Peso (kg):", bg="#FFE6F2", fg="#8A4F7D", font=fonte_titulo).pack(pady=5)
peso_entry = tk.Entry(root, bg="white", relief="flat", font=fonte_normal)
peso_entry.pack(pady=2)

tk.Label(root, text="📏 Altura (m):", bg="#FFE6F2", fg="#8A4F7D", font=fonte_titulo).pack(pady=5)
altura_entry = tk.Entry(root, bg="white", relief="flat", font=fonte_normal)
altura_entry.pack(pady=2)

# Criar a função de cálculo do IMC
def calcular_imc():
    try:
        # Substituir vírgula por ponto antes da conversão
        peso = float(peso_entry.get().replace(",", "."))
        altura = float(altura_entry.get().replace(",", "."))

        if altura <= 0 or peso <= 0:
            messagebox.showerror("🚨 Erro", "Altura e peso devem ser positivos!")
            return

        imc = peso / (altura ** 2)

        # Classificação do IMC com emojis fofos
        if imc < 18.5:
            categoria = "Abaixo do peso 😟"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal 😊"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso 😕"
        elif 30 <= imc < 34.9:
            categoria = "Obesidade Grau 1 😟"
        elif 35 <= imc < 39.9:
            categoria = "Obesidade Grau 2 😧"
        else:
            categoria = "Obesidade Grau 3 😨"

        resultado_label.config(text=f"💖 IMC: {imc:.2f}\n{categoria}", fg="#D72638")

    except ValueError:
        messagebox.showerror("🚨 Erro", "Digite valores numéricos válidos! (Exemplo: 70.5 ou 70,5)")

# Criar botão fofinho
btn_calcular = tk.Button(root, 
                         text="🧁 Calcular IMC", 
                         command=calcular_imc,
                         bg="#FF99C8",  # Rosa médio
                         fg="white",
                         relief="flat",
                         font=fonte_titulo)
btn_calcular.pack(pady=10)

# Criar rótulo para exibir o resultado
resultado_label = tk.Label(root, text="IMC: --", font=fonte_titulo, bg="#FFE6F2", fg="#8A4F7D")
resultado_label.pack(pady=10)

# Rodar a aplicação
root.mainloop()
