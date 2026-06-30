def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def start_ui():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("بەخێر بێن بۆ یاری سێ ڕیزەی کوردی")
    print_board(board)
    choice = input("ژمارەی خانەکە هەڵبژێرە (١-٩): ")
    print(f"تۆ خانەی {choice}ـت هەڵبژارد!")

if __name__ == "__main__":
    start_ui()
