import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                cell = tk.Button(self.master, text='', font=('Arial', 60), width=3, height=1,
                                 command=lambda row=i, col=j: self.mark(row, col))
                cell.grid(row=i, column=j)
                self.board[i][j] = cell

        restart_button = tk.Button(self.master, text='Restart', font=('Arial', 20), command=self.restart)
        restart_button.grid(row=3, column=1)

    def mark(self, row, col):
        if self.board[row][col]['text'] == '' and not self.game_over:
            self.board[row][col].config(text=self.current_player)

            if self.check_win():
                self.game_over = True
                tk.messagebox.showinfo('Tic Tac Toe', f'{self.current_player} wins!')
            elif self.check_tie():
                self.game_over = True
                tk.messagebox.showinfo('Tic Tac Toe', 'It is a tie!')
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        # check rows
        for i in range(3):
            if self.board[i][0]['text'] == self.board[i][1]['text'] == self.board[i][2]['text'] != '':
                return True

        # check columns
        for i in range(3):
            if self.board[0][i]['text'] == self.board[1][i]['text'] == self.board[2][i]['text'] != '':
                return True

        # check diagonals
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            return True
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            return True

        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]['text'] == '':
                    return False
        return True

    def restart(self):
        self.current_player = 'X'
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.board[i][j].config(text='')

if __name__ == '__main__':
    root = tk.Tk()
    tictactoe = TicTacToe(root)
    root.mainloop()

