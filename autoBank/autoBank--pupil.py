import random  # 随机模块


# createNumbers??生成nNum个数量的随机数字
def createNumbers(nNum):
    NumberList = []  # 创建一个随机数列表

    for i in range(0, nNum):  # 循环随机数nNum位

        number = random.randint(0, 100)  # number得到随机数

        NumberList.append(number)  # append是添加 随机数添加到numberList列表

    # print(NumberList)

    return NumberList


# createOperators??生成Openum个数量的随机符号
def createOperators(grade, opeNum):
    operators = ['+', '-', '*', '/']

    operatorList = []  # 创建一个随机符号列表

    if grade == 1 or grade == 2:

        for i in range(0, opeNum):  # 循环随机数opeNum位

            index = random.randint(0, 1)  # index得到随机符号下标

            operatorList.append(operators[index])  # 添加至符号列表
    else:

        for i in range(0, opeNum):  # 循环随机数opeNum位

            index = random.randint(0, 3)  # index得到随机符号下标

            operatorList.append(operators[index])  # 添加至符号列表

    return operatorList


# createProblems??生成一定数量的简单式子,proLength为式子长度，即多少个数字，proNum为式子数量，即多少条
def createSimpleProblems(grade, degreeOfDiff):
    if degreeOfDiff == '1':

        proLength = random.randint(2, 3)  # 难度系数为1

    elif degreeOfDiff == '2':

        proLength = random.randint(4, 5)  # 难度系数为2

    elif degreeOfDiff == '3':

        proLength = random.randint(6, 7)  # 难度系数为3

    elif degreeOfDiff == '4':

        proLength = random.randint(7, 8)  # 难度系数为4

    elif degreeOfDiff == '5':

        proLength = random.randint(9, 10)  # 难度系数为5

    else:

        proLength = random.randint(2, 4)  # 默认难度系数

    numbers = createNumbers(proLength)  # 创建一个随机数列表

    operators = createOperators(grade, proLength - 1)  # 创建一个随机符号列表

    problem = ''  # 四则运算式子

    for i in range(0, len(operators)):  # 循环将随机数和随机符号做拼接

        problem += str(numbers[i]) + ' ' + operators[i] + ' '

    problem += str(numbers[i + 1])

    # print(problem)

    return problem


# 计算式子的单元块结果，elementOne，elementTwo分别为左右数字，operator为符号
def getElementSum(elementOne, elementTwo, operator):
    res = 0

    if operator == '+':  # 加法运算

        res = elementOne + elementTwo

    elif operator == '-':  # 减法运算

        # elementOne,elementTwo=max(elementOne,elementTwo),min(elementOne,elementTwo)        #防止结果为负数

        res = elementOne - elementTwo

    elif operator == '*':  # 乘法运算

        res = elementOne * elementTwo

    else:
        res = elementOne / elementTwo  # 除法运算

    return res


# getSum()??计算每条式子的结果
'''
def getSum(problem):
    
    problemList = problem.split(' ')                #把式子转化成数组
    
    for i in range(0,len(problemList),2):
        
        problemList[i] = int(problemList[i])        #式子数组中数字从字符串转化成整型
        
        #print(problemList[i])    
    
    elementOne = problemList[0]                     #初始化运算左右元素
    
    elementTwo = problemList[2]
    
    operator = problemList[1]
    
    Sum =  0
    
    for i in range(3,len(problemList)-1,2):
        
        elementOne = getElementSum(elementOne,elementTwo,operator)  #每一单元块求和后都重新赋值给左边的元素
        
        elementTwo = problemList[i+1]
        
        operator = problemList[i]
        
    Sum = getElementSum(elementOne,elementTwo,operator)             #最终式子结果

'''


# getSum()??计算每条式子的结果
def getSum(problem):
    Sum = eval(problem)

    if Sum > 0:

        print("题目:" + problem)

        print("正确答案:" + str(Sum))

    else:

        print("题目:" + problem + ' + 10000')  # 如果结果是负数，则加上特定值得到整数

        print("正确答案:" + str(Sum + 10000))

    return Sum


# createProblems??生成num个数量的式子，并判断结果
def createProblems(num, gradeNum, degreeOfDiff):
    for i in range(0, int(num)):  # 生成num个数量式子

        problem = createSimpleProblems(gradeNum, degreeOfDiff)

        trueSum = getSum(problem)

        print("请输入本题的答案:")

        inputSum = input()  # 获取用户输入答案

        trueNum = 0

        if int(inputSum) == int(trueSum):  # 判断对错

            print("答案正确！")

            trueNum += 1

        else:

            print("答案错误！")

        accuracyRate = trueNum / float(num)  # 计算刷题准确率

    print("本次刷题准确率达到{}%".format(accuracyRate * 100))


# 主函数
def main():
    print("??????小学生四则运算自动刷题库??????")

    print("请输入您的所在年级:(1,2,3,4,5,6)")

    gradeNum = input()

    print("请输入您要选择的难易程度:(1,2,3,4,5->简单，较易，中等，较难，难)")

    degreeOfDiff = input()

    print("请输入本次刷题目标数量:")

    problemNum = input()

    createProblems(problemNum, gradeNum, degreeOfDiff)


if __name__ == '__main__':
    main()
