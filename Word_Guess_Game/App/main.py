import tkinter as tk

class Guess_Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Board()

    def Board(self):
        Frame  = tk.Frame(master=self)
        Frame.pack(fill=tk.X)

def main():
    game = Guess_Game()
    game.mainloop()

if __name__ == '__main__':
    main()
