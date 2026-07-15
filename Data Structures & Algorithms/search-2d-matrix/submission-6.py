class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:    
        t,b=0,len(matrix)-1

        while t<=b:
            m=(t+b)//2
            
            if matrix[m][0]>target:
                b=m-1
            elif matrix[m][0]<target:
                t=m+1
            else:
                print("GOTCHA")
                return True

        if b<0:
            return False
        else:
            m=b

        l,r=0,len(matrix[0])-1
        while l<=r:
            m2=(l+r)//2
            
            if matrix[m][m2]>target:
                r=m2-1
            elif matrix[m][m2]<target:
                l=m2+1
            else:
                return True
        return False

            
