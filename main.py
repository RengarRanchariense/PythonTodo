import tkinter as tk
from tkinter import ttk, font, messagebox



# criando janela
janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

frame_em_edicao = None

#função adcionar tarefas

def adcionar_tarefa():
    global frame_em_edicao
    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0 , tk.END)
            
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, Insira uma tarefa")
        
        
def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)
    label_tarefa = tk.Label(frame_tarefa, text=tarefa,font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)
    
    botao_editar = tk.Button(frame_tarefa, text="Editar", bg="#4CAF50", fg="white", height=1, width=4, font=("Roboto", 11), relief=tk.FLAT, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l))
    botao_editar.pack(side=tk.RIGHT, padx=5)
    botao_deletar = tk.Button(frame_tarefa, text="Deletar", bg="red", fg="white", height=1, width=4, font=("Roboto", 11), relief=tk.FLAT, command=lambda f=frame_tarefa:deletar_tarefa(f))
    botao_deletar.pack(side=tk.RIGHT, padx=5)
    
    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)
    
    checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_sublinhado(label))
    checkbutton.pack(side=tk.RIGHT, padx=5)
    
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))
    
    
def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=nova_tarefa)
            
def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
def alterar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace(" overstrike", "")
    else:
        nova_fonte = fonte_atual + " overstrike"
    label.config(font=nova_fonte)
    
    
    


fonte_cabecalho = font.Font(family="Garamond", size=24,weight="bold")
rotulo_cabecalho = tk.Label(janela, text="APLICATIVO DE TAREFAS", font=fonte_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20)



frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(pady=10)
entrada_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

botao_adcionar = tk.Button(frame, command= adcionar_tarefa,text="Adcionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adcionar.pack(side=tk.LEFT, padx=10)

#Criar um frae para a lista de tarefas com rolagem

frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


canvas = tk.Canvas(frame_lista_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


scrollbar = tk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))







janela.mainloop()