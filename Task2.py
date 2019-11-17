N = float(input('Enter number of students: '))
K = float(input('Enter number of apples: '))

forStud=(K/N)
student=str(forStud)
forBasket=(K%N)
basket=str(forBasket)
print('Sum of apples for each student: '+ student)
print('Sum of apples in basket: '+ basket )
