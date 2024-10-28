class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create three dictionaries
        rowDict = defaultdict(list) # row numbers
        colDict = defaultdict(list) # column numbers
        squareDict = defaultdict(list) # square numbers

        # Loop through the whole board
        for row in range(len(board)):
            for col in range(len(board)):
                # Get the number
                num = board[row][col]

                # Has it been seen in the current row before?
                if num in rowDict[row]:
                    return False # yes, invalid board

                # ... current column before?
                if num in colDict[col]:
                    return False

                # ... current square before?
                if num in squareDict[(row//3) + 3 * (col//3)]:
                    return False
                
                # Record the number in each location if it's a number
                if num != ".":
                    rowDict[row].append(num)
                    colDict[col].append(num)
                    squareDict[(row//3) + 3 * (col//3)].append(num)
        
        # All tiles checked, looks good!
        return True