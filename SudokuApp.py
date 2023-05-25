import tkinter as tk
import random

class SudokuApp:
    def __init__(self, nivel_dificultad):
        self.nivel_dificultad = nivel_dificultad
        self.puzzle = self.generar_puzzle()
        
        self.ventana = tk.Tk()
        self.ventana.title("Sudoku")
        
        self.cuadros = []
        
        for i in range(9):
            fila = []
            for j in range(9):
                valor = self.puzzle[i][j]
                if valor == 0:
                    cuadro = tk.Entry(self.ventana, width=3, font=("Arial", 16))
                    cuadro.grid(row=i, column=j)
                else:
                    cuadro = tk.Label(self.ventana, text=str(valor), width=3, font=("Arial", 16))
                    cuadro.grid(row=i, column=j)
                fila.append(cuadro)
            self.cuadros.append(fila)
        
        boton_validar = tk.Button(self.ventana, text="Validar", command=self.validar_puzzle)
        boton_validar.grid(row=9, column=0, columnspan=9)
        
    def generar_puzzle(self):
        puzzles = {
            "Fácil": [
                [0, 2, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 0, 0, 7, 5, 0, 9, 0],
                [0, 0, 0, 1, 0, 0, 0, 8, 0],
                [0, 9, 0, 0, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 2, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 0, 0, 1, 0, 0, 0, 3],
                [0, 0, 9, 0, 0, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 4, 0, 0]
            ],
            "Medio": [
                [0, 0, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 0, 0, 0, 5, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 2, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 9, 0, 0, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 4, 0, 0]
            ],
            "Difícil": [
                [0, 0, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 0, 0, 0, 5, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 2, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 9, 0, 0, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 4, 0, 0]
            ],
            "Experto": [
                [0, 0, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 0, 0, 0, 5, 0, 9, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 0, 0],
                [8, 0, 0, 0, 2, 0, 0, 0, 0],
                [7, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 9, 0, 0, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 4, 0, 0]
            ]
        }
        
        return puzzles[self.nivel_dificultad]
    
    def validar_puzzle(self):
        for i in range(9):
            for j in range(9):
                cuadro = self.cuadros[i][j]
                if cuadro.winfo_class() == "Entry":
                    valor = cuadro.get()
                    if valor != str(self.puzzle[i][j]):
                        cuadro.config(bg="red")
                    else:
                        cuadro.config(bg="white")

nivel_dificultad = input("Selecciona un nivel de dificultad (Fácil, Medio, Difícil, Experto): ")
sudoku_app = SudokuApp(nivel_dificultad)
sudoku_app.ventana.mainloop()
