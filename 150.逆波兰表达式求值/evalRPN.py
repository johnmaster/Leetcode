"""
执行用时 :144 ms, 在所有 python3 提交中击败了39.37%的用户
内存消耗 :14.1 MB, 在所有 python3 提交中击败了5.23%的用户

逆波兰表达式计算：
1.从左到右顺序扫描整个后缀表达式
2.如果是操作数，则将该操作数压入栈中
3.如果是操作符，则从栈中弹出对应的操作数，注意操作数的顺序，根据操作符进行运算，并
将结果重新压入到栈中
4.直至将整个栈扫描完毕
5.如果后缀表达式是合法的，则扫描完毕后，栈中只有一个元素，该元素的值即为后缀表达式的结果

python不能简单的通过内置函数判断负数是否是数字
"""
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(eval(b + i + a))))
            else:
                stack.append(i)
        return stack[-1]
