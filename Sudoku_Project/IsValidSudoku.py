class IsValidSudoku:
    __sudokuPuzzle = [[0]*9]*9
    
        
    
    def __init__(self, puzzle):
    #Copy 2D array to the private array   
        for x in range(1, 9):
            for y in range(1, 9):
    #Check if out of bounds
                if(puzzle[x][y] <= 0 or puzzle[x][y] > 9):
                    print(f'Index [{x}][{y}] is out of range.\nMust be between 1 and 9\n')
                self.__sudokuPuzzle = puzzle[x][y]
                    
    #3x3 grid check
   
    #rows check
    def rowCheck(self):
    # check entire board
        for row in range(1,9):
            for col in range(1,9):
    #grab number and check if it repeats
                temp = self.__sudokuPuzzle[row][col]
                occur = 0
                for x in range(1,9):
                    if temp == self.__sudokuPuzzle[row][x]:
                        occur += 1
                        if occur > 1:
                            return False
        return True
                    
    #column check
    

    #run method for threads
    
    