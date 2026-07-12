class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=len(board[0])

        for row in board:
            nums=[x for x in row if x!='.']
            if len(nums)!=len(set(nums)):
                return False

        for i in range(0,cols):
            nums=[]
            for row in board:
                if row[i]!='.':
                    nums.append(row[i])
            if len(nums)!=len(set(nums)):
                return False

        for box_col in range(0,9,3):
            for box_row in range(0,9,3):
                nums=[]
                for j in range(box_col, box_col+3):
                    for i in range(box_row, box_row+3):
                        if board[i][j]!='.':
                            nums.append(board[i][j])
                if len(nums)!=len(set(nums)):
                                return False
        return True