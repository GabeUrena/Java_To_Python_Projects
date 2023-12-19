import unittest
from IsValidSudoku import IsValidSudoku


class TestIsValidSudoku(unittest.TestCase):
    
    matrix1 = [[6, 2, 4, 5, 3, 9, 1, 8, 7],
			    [5, 1, 9, 7, 2, 8, 6, 3, 4],
				[8, 3, 7, 6, 1, 4, 2, 9, 5],
				[1, 4, 3, 8, 6, 5, 7, 2, 9],
				[9, 5, 8, 2, 4, 7, 3, 6, 1],
				[7, 6, 2, 3, 9, 1, 4, 5, 8],
				[3, 7, 1, 9, 5, 6, 8, 4, 2],
				[4, 9, 6, 1, 8, 2, 5, 7, 3],
				[2, 8, 5, 4, 7, 3, 9, 1, 6]]
    
    
    matrix2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9],
			    [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    
    
    matrix3 = [[9, 9, 9, 9, 9, 9, 9, 9, 9],
			    [8, 8, 8, 8, 8, 8, 8, 8, 8],
			    [7, 7, 7, 7, 7, 7, 7, 7, 7],
			    [6, 6, 6, 6, 6, 6, 6, 6, 6],
			    [5, 5, 5, 5, 5, 5, 5, 5, 5],
			    [4, 4, 4, 4, 4, 4, 4, 4, 4],
			    [3, 3, 3, 3, 3, 3, 3, 3, 3],
			    [2, 2, 2, 2, 2, 2, 2, 2, 2],
			    [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    matrix4 = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
				[4, 5, 6, 4, 5, 6, 4, 5, 6],
				[7, 8, 9, 7, 8, 9, 7, 8, 9],
				[1, 2, 3, 1, 2, 3, 1, 2, 3],
				[4, 5, 6, 4, 5, 6, 4, 5, 6],
				[7, 8, 9, 7, 8, 9, 7, 8, 9],
				[1, 2, 3, 1, 2, 3, 1, 2, 3],
				[4, 5, 6, 4, 5, 6, 4, 5, 6],
				[7, 8, 9, 7, 8, 9, 7, 8, 9]]
    
    
    sudoku1 = IsValidSudoku(matrix1) # all true
    sudoku2 = IsValidSudoku(matrix2) # only rows pass
    sudoku3 = IsValidSudoku(matrix3) # only columns pass
    sudoku4 = IsValidSudoku(matrix4) # only grids pass
        
    def test_gridCheck(self):
        self.assertTrue(self.sudoku1.gridCheck())
        self.assertFalse(self.sudoku2.gridCheck())
        self.assertFalse(self.sudoku3.gridCheck())
        self.assertTrue(self.sudoku4.gridCheck())
         
    def test_rowCheck(self):
        self.assertTrue(self.sudoku1.rowCheck())
        self.assertTrue(self.sudoku2.rowCheck())
        self.assertFalse(self.sudoku3.rowCheck())
        self.assertFalse(self.sudoku4.rowCheck())
        
    def test_columnCheck(self):
        self.assertTrue(self.sudoku1.columnCheck())
        self.assertFalse(self.sudoku2.columnCheck())
        self.assertTrue(self.sudoku3.columnCheck())
        self.assertFalse(self.sudoku4.columnCheck())
          
        
if __name__ == '__main__':
     unittest.main()