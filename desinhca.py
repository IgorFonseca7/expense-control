import tkinter as tk
from tkinter import ttk
from datetime import datetime

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Despesas")

        self.despesas = []

        self.frame_esquerda = tk.Frame(root)
        self.frame_esquerda.grid(row=0, column=0, sticky='n')

        self.label_despesa = tk.Label(self.frame_esquerda, text="Nome da despesa")
        self.label_despesa.pack()

        self.entry_despesa = tk.Entry(self.frame_esquerda, font=('Arial', 14), width=30)
        self.entry_despesa.pack()

        self.label_empresa = tk.Label(self.frame_esquerda, text="Empresa")
        self.label_empresa.pack()

        self.entry_empresa = tk.Entry(self.frame_esquerda, font=('Arial', 14), width=30)
        self.entry_empresa.pack()

        self.label_valor = tk.Label(self.frame_esquerda, text="Valor")
        self.label_valor.pack()

        self.entry_valor = tk.Entry(self.frame_esquerda, font=('Arial', 14), width=30)
        self.entry_valor.pack()

        self.label_servico = tk.Label(self.frame_esquerda, text="Serviço")
        self.label_servico.pack()

        self.entry_servico = tk.Entry(self.frame_esquerda, font=('Arial', 14), width=30)
        self.entry_servico.pack()

        self.button = tk.Button(self.frame_esquerda, text="Adicionar", command=self.adicionar_despesa)
        self.button.pack()
        

        self.frame_direita = tk.Frame(root)
        self.frame_direita.grid(row=0, column=1, sticky='n')

        self.tree = ttk.Treeview(self.frame_direita, columns=('Despesa', 'Empresa', 'Serviço', 'Valor', 'Data'), show='headings')
        self.tree.heading('Despesa', text='Despesa')
        self.tree.heading('Empresa', text='Empresa')
        self.tree.heading('Valor', text='Valor')
        self.tree.heading('Serviço', text='Serviço')
        self.tree.heading('Data', text='Data')
        self.tree.pack()

        self.label_total = tk.Label(self.frame_direita, text="Total: R$0.00")
        self.label_total.pack()

    def adicionar_despesa(self):
        despesa = self.entry_despesa.get()
        empresa = self.entry_empresa.get()
        valor = float(self.entry_valor.get())
        servico = self.entry_servico.get()
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Adiciona a data e hora atual

        self.despesas.append((despesa, valor, servico, empresa, data))
        self.tree.insert('', 'end', values=(despesa, valor, servico, empresa, data))

        total = sum(valor for _, valor, _, _, _ in self.despesas)
        self.label_total.config(text=f"Total: R${total:.2f}")

        self.entry_despesa.delete(0, tk.END)
        self.entry_empresa.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_servico.delete(0, tk.END)

root = tk.Tk()
app = App(root)
root.mainloop()
