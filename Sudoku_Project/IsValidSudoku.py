import numpy as np
class IsValidSudoku:
    __sudokuPuzzle = [[0]*9]*9
    
        
    def __init__(self, puzzle):
    #Copy 2D array to the private array   
        for x in range(1, 9):
            for y in range(1, 9):
    #Check if out of bounds
                if(puzzle[x][y] <= 0 or puzzle[x][y] > 9):
                    print(f'Index [{x}][{y}] is out of range.\nMust be between 1 and 9\n')
                self.__sudokuPuzzle[x][y] = puzzle[x][y]
                    
                    
    #3x3 grid check
    def gridCheck(self):
        print("Running grid check")
        tempArr = np.arange(10)
        for segRow in range(1, 9, 3):  
            for segCol in range(1, 9, 3):
                tempArr.fill(False)         
    # Checking each number in each grid
                for gridRow in range(1,3):
                    for gridCol in range(1,3):
    #grab number, if that number shows up multiple times return false
                        num = self.__sudokuPuzzle[segRow+gridRow][segCol+gridCol]
                        if(tempArr[num]):
                            return False
                        tempArr[num]=True
        return True
    
    
    #rows check
    def rowCheck(self):
        print("Running row check")
    # check entire board
        for row in range(1,9):
            for col in range(1,9):
    #grab number and check if it repeats
                temp = self.__sudokuPuzzle[row][col]
                print(f'{temp} is the temp')
                occur = 0
                print(f'{occur} occurances')
                print('start of for loop')
                for x in range(1,9):
                    if temp == self.__sudokuPuzzle[row][x]:
                        print(f'{temp} is equal to sudokuPuzzle: {self.__sudokuPuzzle[row][x]}')
                        occur += 1
                        print(occur)
                        if occur > 1:
                            return False
        return True
                    
                    
    #column check
    def columnCheck(self):
        print("Running col check")
    # check entire board
        for col in range(1,9):
            for row in range(1,9):
    #grab number and check if it repeats
                temp = self.__sudokuPuzzle[row][col]
                occur = 0
                for x in range(1,9):
                    if temp == self.__sudokuPuzzle[x][col]:
                        occur += 1
                        if occur > 1:
                            return False
        return True

    #run method for threads
    
puzzleInput = [ [1, 1, 1, 1, 1, 1, 1, 1, 1],
			    [1, 1, 1, 1, 1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1, 1, 1, 1, 1],
				[1, 1, 1, 1, 1, 1, 1, 1, 1],
				[9, 5, 8, 2, 4, 7, 3, 6, 1],
				[7, 6, 2, 3, 9, 1, 4, 5, 8],
				[3, 7, 1, 1, 5, 6, 8, 4, 2],
				[4, 9, 6, 1, 8, 2, 5, 7, 3],
				[2, 8, 5, 4, 7, 3, 9, 1, 6] ]
        
sudokuValidator = IsValidSudoku(puzzleInput)
        
#print(sudokuValidator.columnCheck())
print(sudokuValidator.rowCheck())
#print(sudokuValidator.gridCheck())
        
        