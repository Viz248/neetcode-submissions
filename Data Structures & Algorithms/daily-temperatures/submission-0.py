class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i,a in enumerate(temperatures):
            j=i
            l=len(temperatures)
            while j<l:
                if temperatures[j]>a:
                    result.append(j-i)
                    break
                elif j==l-1:
                    result.append(0)
                    break
                else:
                    j+=1
        return result