class Solution {
  void solveSudoku(List<List<String>> board) {
    _solve(board);
  }

  bool _solve(List<List<String>> board) {
    for (int row = 0; row < 9; row++) {
      for (int col = 0; col < 9; col++) {
        if (board[row][col] == ".") {
          for (int num = 1; num <= 9; num++) {
            String char = num.toString();
            if (_isValid(board, row, col, char)) {
              board[row][col] = char;
              if (_solve(board)) return true;
              board[row][col] = ".";
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  bool _isValid(List<List<String>> board, int row, int col, String char) {
    for (int i = 0; i < 9; i++) {
      if (board[row][i] == char || board[i][col] == char) return false;
    }
    int startRow = (row ~/ 3) * 3;
    int startCol = (col ~/ 3) * 3;
    for (int i = startRow; i < startRow + 3; i++) {
      for (int j = startCol; j < startCol + 3; j++) {
        if (board[i][j] == char) return false;
      }
    }
    return true;
  }
}