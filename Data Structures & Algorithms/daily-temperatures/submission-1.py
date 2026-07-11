class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[]
        for i in reversed(temperatures):
            if not stack:
                stack.append((i,0))
                result.append(0)
                print(stack[-1])
            elif i<stack[-1][0]:
                stack.append((i,1))
                result.append(1)
            else:
                count=1
                while i>=stack[-1][0]:
                    x=stack.pop()
                    count+=x[1]
                    if not stack:
                        count=0
                        break
                stack.append((i,count))
                result.append(count)
        print(stack)
        print(result)
        result.reverse()
        return result
