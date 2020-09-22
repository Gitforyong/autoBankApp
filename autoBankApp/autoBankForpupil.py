#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random                                         #随机模块
from fractions import Fraction                        #真分数


# In[2]:


#createNumbers——生成nNum个数量的随机数字
def createNumbers(nNum):
    
    NumberList = []                                   #创建一个随机数列表
    
    for i in range(0,nNum):                           #循环随机数nNum位
        
        number = random.randint(0,100)                #number得到随机数
        
        NumberList.append(number)                     #append是添加 随机数添加到numberList列表
        
    #print(NumberList)
    
    return NumberList


# In[3]:


#createOperators——生成OpeNum个数量的随机符号
def createOperators(grade,opeNum):
    
    operators = ['+','-','*','/']
    
    operatorList = []                                    #创建一个随机符号列表
    
    if grade == 1 or grade == 2:
        
        for i in range(0,opeNum):                       #循环随机数opeNum位
            
            index = random.randint(0,1)                 #index得到随机符号下标
        
            operatorList.append(operators[index])       #添加至符号列表
    else:
        
            for i in range(0,opeNum):                       #循环随机数opeNum位
                
                index = random.randint(0,3)                 #index得到随机符号下标
        
                operatorList.append(operators[index])       #添加至符号列表
    
    return operatorList


# In[40]:


#createSimpleProblems——生成一定数量的简单式子,proLength为式子长度，即多少个数字，grade，即年级，degreeOfDiff，难度等级
def createSimpleProblems(grade,degreeOfDiff):
    
    if degreeOfDiff == '1':                              
        
        proLength = random.randint(2,3)                #难度系数为1
        
    elif degreeOfDiff == '2':
        
        proLength = random.randint(4,5)                #难度系数为2
        
    elif degreeOfDiff == '3':
        
        proLength = random.randint(6,7)                #难度系数为3
        
    elif degreeOfDiff == '4':
        
        proLength = random.randint(7,8)                #难度系数为4
        
    elif degreeOfDiff == '5':
        
        proLength = random.randint(9,10)               #难度系数为5
    
    else:
        
        proLength = random.randint(2,4)                #默认难度系数        
        
    numbers = createNumbers(proLength)               #创建一个随机数列表
    
    operators = createOperators(grade,proLength-1)   #创建一个随机符号列表
    
    problem = ''                                     #四则运算式子
    
    for i in range(0,len(operators)):                #循环将随机数和随机符号做拼接
        
        problem += str(numbers[i]) + ' ' + operators[i] + ' '    
        
    problem += str(numbers[i+1])    
        
    if eval(problem) < 0:
        
        createSimpleProblems(grade,degreeOfDiff)
    
    else:
        
        return problem


# In[44]:


# createProperFractionPro——生成真分数加减问题
def createProperFractionPro(num,degree):
    
    operator = ['+', '-']
    
    if degree == '1':
        
        degree = random.randint(1, 2)                #难度系数为1
    
    elif degree == '2':
        
        degree = random.randint(3, 4)                #难度系数为2
        
    elif degree == '3':
        
        degree = random.randint(5, 6)                #难度系数为3
        
    elif degree == '4':
        
        degree = random.randint(7, 8)                #难度系数为4
        
    elif degree == '5':
        
        degree = random.randint(9, 10)               #难度系数为5
    
    else:
        
        degree = random.randint(1, 3)                #默认难度系数
    
    problem = ''
    
    trueNum = 0
    
    for i in range(degree):
        
        numerator = random.randint(1, 10)                             #随机生成分子
        
        denominator = random.randint(numerator, 10)                   #真分数要求分子小于分母
        
        operatorT = operator[random.randint(0, 1)]                    #只要求+ -
        
        problem += str(numerator) + '/' + str(denominator) + operatorT  #拼接成一个问题

    numerator = random.randint(1, 10)                                   #最后一个分数
    
    denominator = random.randint(numerator, 10)
    
    problem += str(numerator) + '/' + str(denominator)
    
    Sum = eval(problem)
    
    Sum = Fraction('{}'.format(Sum)).limit_denominator()

    if Sum > 0:
        
        print("题目:"+ problem , "=")
        
        #print('正确的答案为：',Sum)
        
        print("请输入本题的答案:")   
        
        inputSum = Fraction('{}'.format(eval(input()))).limit_denominator()   #获取用户输入的答案
        
        if Sum == inputSum:
            
            trueNum = 1
            
            print("答案正确！")
            
        else:
            
            trueNum = 0
            
            print("答案错误！")
            
            print('正确的答案为：',Sum)
            
    else:                                                              #如果结果是负数，则重新生成
        
        createProperFractionPro(num,degree)
        
    #print("fanhuide="+str(trueNum))
    
    return trueNum


# In[45]:


#createProblems——生成num个数量的式子，并判断结果,type
def createProblems(num,titleType,gradeNum,degreeOfDiff):
    
    trueAcc = 0
    
    for i in range(0,int(num)):                                         #生成num个数量式子
            
        if titleType == '1':
            
            problem = createSimpleProblems(gradeNum,degreeOfDiff)
            
            trueSum = int(eval(str(problem)))
            
            #trueSum = Fraction('{}'.format(trueSum)).limit_denominator()         #计算正确答案

            print("题目:"+ problem + "=")
            
            #print('正确的答案为：',trueSum)
        
            print("请输入本题的答案:")                                    
        
            #inputSum = Fraction('{}'.format(eval(input()))).limit_denominator()   #获取用户输入的答案 
            
            inputSum = int(eval(input()))
        
            if inputSum == trueSum:                                                 #判断对错
            
                trueAcc += 1
                
                #print("every"+str(trueAcc))
            
                print("答案正确！")
 
            else:
            
                print("答案错误！")
            
                print('正确的答案为：',trueSum)                          
                
        else:
            
            tempNum = createProperFractionPro(num,degreeOfDiff)
            
            trueAcc = trueAcc + tempNum
            
            #print("trueAcc="+str(trueAcc))
        
            
    accuracyRate = trueAcc/float(num)       #计算刷题准确率
    
    print("您本次刷题准确率达到{}%".format(accuracyRate*100))
    


# In[46]:


#主函数
def main():
    
    print("——————小学生四则运算自动刷题库——————")
    
    print("请输入您的所在年级:(1,2,3,4,5,6)")
    
    gradeNum = input()
    
    print("请输入本次刷题题型:1,0->(100以内正整数四则运算，真分数加减运算)")
    
    title = input()
    
    print("请输入您要选择的难易程度:(1,2,3,4,5->简单，较易，中等，较难，难)")
    
    degreeOfDiff = input()
    
    print("请输入本次刷题目标数量:")
    
    problemNum = input()
            
    createProblems(problemNum,title,gradeNum,degreeOfDiff)

if __name__ ==  '__main__':
    main()







