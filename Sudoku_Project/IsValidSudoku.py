class IsValidSudoku:
    
    
        
    #Constructor + check if puzzle is a 9x9
    def __init__(self, puzzle):
        for x in range(1, 9):
            for y in range(1, 9):
                if(puzzle[x][y] <= 0 or puzzle[x][y] > 9):
                    print(f'Index [{x}][{y}] is out of range.\nMust be between 1 and 9\n')
                    
                    
    #3x3 grid check
    
    #rows check
    
    #column check
    

    #run method for threads