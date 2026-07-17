class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. Check the row
        for r in range(9):
            seen = set()
            for c in range(9):

                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                else:
                    seen.add(val)

    
        # 2. Check the columns

        for c in range(9):
            seen = set()
            for r in range(9):

                val = board[r][c]
                if val == ".":
                    continue
                if val in seen:
                    return False
                else:
                    seen.add(val)

        
        
        
        # 3. Check the 3x3s. 
        # Loop through each 3x3.
        for box_x in range(0, 9, 3): 
            for box_y in range(0, 9, 3):

                seen = set()

                # Loop through the 3x3
                for r in range(3): # go right
                    for c in range(3): # go down
                        
                        val = board[box_x + r][box_y + c]
                        # Ignore Blank spaces
                        if val == ".":
                            continue
                        # Check for duplicate vals. 
                        if val in seen:
                            return False
                        else:
                            seen.add(val)

        
        return True