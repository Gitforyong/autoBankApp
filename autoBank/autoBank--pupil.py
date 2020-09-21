import random  # ���ģ��


# createNumbers??����nNum���������������
def createNumbers(nNum):
    NumberList = []  # ����һ��������б�

    for i in range(0, nNum):  # ѭ�������nNumλ

        number = random.randint(0, 100)  # number�õ������

        NumberList.append(number)  # append����� �������ӵ�numberList�б�

    # print(NumberList)

    return NumberList


# createOperators??����Openum���������������
def createOperators(grade, opeNum):
    operators = ['+', '-', '*', '/']

    operatorList = []  # ����һ����������б�

    if grade == 1 or grade == 2:

        for i in range(0, opeNum):  # ѭ�������opeNumλ

            index = random.randint(0, 1)  # index�õ���������±�

            operatorList.append(operators[index])  # ����������б�
    else:

        for i in range(0, opeNum):  # ѭ�������opeNumλ

            index = random.randint(0, 3)  # index�õ���������±�

            operatorList.append(operators[index])  # ����������б�

    return operatorList


# createProblems??����һ�������ļ�ʽ��,proLengthΪʽ�ӳ��ȣ������ٸ����֣�proNumΪʽ����������������
def createSimpleProblems(grade, degreeOfDiff):
    if degreeOfDiff == '1':

        proLength = random.randint(2, 3)  # �Ѷ�ϵ��Ϊ1

    elif degreeOfDiff == '2':

        proLength = random.randint(4, 5)  # �Ѷ�ϵ��Ϊ2

    elif degreeOfDiff == '3':

        proLength = random.randint(6, 7)  # �Ѷ�ϵ��Ϊ3

    elif degreeOfDiff == '4':

        proLength = random.randint(7, 8)  # �Ѷ�ϵ��Ϊ4

    elif degreeOfDiff == '5':

        proLength = random.randint(9, 10)  # �Ѷ�ϵ��Ϊ5

    else:

        proLength = random.randint(2, 4)  # Ĭ���Ѷ�ϵ��

    numbers = createNumbers(proLength)  # ����һ��������б�

    operators = createOperators(grade, proLength - 1)  # ����һ����������б�

    problem = ''  # ��������ʽ��

    for i in range(0, len(operators)):  # ѭ��������������������ƴ��

        problem += str(numbers[i]) + ' ' + operators[i] + ' '

    problem += str(numbers[i + 1])

    # print(problem)

    return problem


# ����ʽ�ӵĵ�Ԫ������elementOne��elementTwo�ֱ�Ϊ�������֣�operatorΪ����
def getElementSum(elementOne, elementTwo, operator):
    res = 0

    if operator == '+':  # �ӷ�����

        res = elementOne + elementTwo

    elif operator == '-':  # ��������

        # elementOne,elementTwo=max(elementOne,elementTwo),min(elementOne,elementTwo)        #��ֹ���Ϊ����

        res = elementOne - elementTwo

    elif operator == '*':  # �˷�����

        res = elementOne * elementTwo

    else:
        res = elementOne / elementTwo  # ��������

    return res


# getSum()??����ÿ��ʽ�ӵĽ��
'''
def getSum(problem):
    
    problemList = problem.split(' ')                #��ʽ��ת��������
    
    for i in range(0,len(problemList),2):
        
        problemList[i] = int(problemList[i])        #ʽ�����������ִ��ַ���ת��������
        
        #print(problemList[i])    
    
    elementOne = problemList[0]                     #��ʼ����������Ԫ��
    
    elementTwo = problemList[2]
    
    operator = problemList[1]
    
    Sum =  0
    
    for i in range(3,len(problemList)-1,2):
        
        elementOne = getElementSum(elementOne,elementTwo,operator)  #ÿһ��Ԫ����ͺ����¸�ֵ����ߵ�Ԫ��
        
        elementTwo = problemList[i+1]
        
        operator = problemList[i]
        
    Sum = getElementSum(elementOne,elementTwo,operator)             #����ʽ�ӽ��

'''


# getSum()??����ÿ��ʽ�ӵĽ��
def getSum(problem):
    Sum = eval(problem)

    if Sum > 0:

        print("��Ŀ:" + problem)

        print("��ȷ��:" + str(Sum))

    else:

        print("��Ŀ:" + problem + ' + 10000')  # �������Ǹ�����������ض�ֵ�õ�����

        print("��ȷ��:" + str(Sum + 10000))

    return Sum


# createProblems??����num��������ʽ�ӣ����жϽ��
def createProblems(num, gradeNum, degreeOfDiff):
    for i in range(0, int(num)):  # ����num������ʽ��

        problem = createSimpleProblems(gradeNum, degreeOfDiff)

        trueSum = getSum(problem)

        print("�����뱾��Ĵ�:")

        inputSum = input()  # ��ȡ�û������

        trueNum = 0

        if int(inputSum) == int(trueSum):  # �ж϶Դ�

            print("����ȷ��")

            trueNum += 1

        else:

            print("�𰸴���")

        accuracyRate = trueNum / float(num)  # ����ˢ��׼ȷ��

    print("����ˢ��׼ȷ�ʴﵽ{}%".format(accuracyRate * 100))


# ������
def main():
    print("??????Сѧ�����������Զ�ˢ���??????")

    print("���������������꼶:(1,2,3,4,5,6)")

    gradeNum = input()

    print("��������Ҫѡ������׳̶�:(1,2,3,4,5->�򵥣����ף��еȣ����ѣ���)")

    degreeOfDiff = input()

    print("�����뱾��ˢ��Ŀ������:")

    problemNum = input()

    createProblems(problemNum, gradeNum, degreeOfDiff)


if __name__ == '__main__':
    main()
