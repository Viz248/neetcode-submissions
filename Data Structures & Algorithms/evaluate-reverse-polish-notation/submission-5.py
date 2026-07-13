class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
                print(stack)
            elif i=="-":
                stack.append(-stack.pop()+stack.pop())
                print(stack)
            elif i=="*":
                stack.append(stack.pop()*stack.pop())
                print(stack)
            elif i=="/":
                a=stack.pop()
                b=stack.pop()
                print(a,b)
                stack.append(int(b/a))
                print(stack)
            else:
                stack.append(int(i))
        return stack[0]