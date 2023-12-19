import numpy as np
import threading


class IsValidSudoku:
    __sudokuPuzzle = [ [0, 0, 0, 0, 0, 0, 0, 0, 0],
			    [0, 0,0 , 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 1, 0, 0, 0],
				[0, 0, 0, 0, 0, 6, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0] ]
        
  
    def __init__(self, puzzle):
        #Copy 2D array to the private array   
        for x in range(0, 9):
            for y in range(0, 9):
    #Check if out of bounds
                if(puzzle[x][y] <= 0 or puzzle[x][y] > 9):
                    print(f'Index [{x}][{y}] is out of range.\nMust be between 1 and 9\n')           
                self.__sudokuPuzzle[x][y] = puzzle[x][y]
                    
         
    #3x3 grid check
    def gridCheck(self):
        print("Running grid check")
        tempArr = np.arange(10)
        for segRow in range(0, 9, 3):  
            for segCol in range(0, 9, 3):
                tempArr.fill(False)         
    # Checking each number in each grid
                for gridRow in range(0,3):
                    for gridCol in range(0,3):
    #grab number, if that number shows up multiple times return false
                        num = self.__sudokuPuzzle[segRow+gridRow][segCol+gridCol]
                        if(tempArr[num]):
                            print('Grid Check: False')
                            return False
                        tempArr[num]=True
        print('Column Check: True')
        return True
    
    
    #rows check
    def rowCheck(self):
        print("Running row check")
    # check entire board
        for row in range(0,9):
            for col in range(0,9):
    #grab number and check if it repeats
                temp = self.__sudokuPuzzle[row][col]
                occur = 0
                for x in range(0,9):
                    if temp == self.__sudokuPuzzle[row][x]:
                        occur += 1
                        if occur > 1:
                            print('Row Check: False')
                            return False
        print('Row Check: True')
        return True
    
    def sum (self):
        return 1
                    
    #column check
    def columnCheck(self):
        print("Running col check")
    # check entire board
        for col in range(0,9):
            for row in range(0,9):
    #grab number and check if it repeats
                temp = self.__sudokuPuzzle[row][col]
                occur = 0
                for x in range(0,9):
                    if temp == self.__sudokuPuzzle[x][col]:
                        occur += 1
                        if occur > 1:
                            print('Column Check: False')
                            return False
        print('Column Check: True')
        return True

    #run method for threads
    def threadrun (self):
        thread1 = threading.Thread(target = self.columnCheck)
        thread2 = threading.Thread(target = self.rowCheck)
        thread3 = threading.Thread(target = self.gridCheck)
        
        print('******* Starting Threads *******')
        
        thread1.start()
        thread2.start()
        thread3.start()
        
        thread1.join()
        thread2.join()
        thread3.join()
        
        print('******* Threads complete *******')
        
"""
puzzleInput = [[1, 2, 3, 1, 2, 3, 1, 2, 3],
				[4, 5, 6, 4, 5, 6, 4, 5, 6],
				[7, 8, 9, 7, 8, 9, 7, 8, 9],
				[1, 2, 3, 1, 2, 3, 1, 2, 3],
				[4, 5, 6, 4, 5, 6, 4, 5, 6],
				[7, 8, 9, 7, 8, 9, 7, 8, 9],
				[1, 2, 3, 1, 2, 3, 1, 2, 3],
				[4, 5, 6, 4, 5, 6, 4, 5, 6],
				[7, 8, 9, 7, 8, 9, 7, 8, 9]]
                    
sudokuValidator = IsValidSudoku(puzzleInput)

sudokuValidator.threadrun()
  """     