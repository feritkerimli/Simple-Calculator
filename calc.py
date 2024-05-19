# Simple calc funksiyalari

# Toplama
def addition():

    # Elementleri bir sətirdə boşluqlarla ayrilmış səkildə götürür
    list_of_sum= [float(num) for num in input("Enter the elements, separate with a space: ").split()]
    print(sum(list_of_sum)) # Sum funksiyası ilə cəmi tapıb print ilə çap edir.

# Çıxma
def subtraction():
    descending = float(input("Enter the descending:")) # Azalan
    subtracted=float(input("Enter the subtracted:"))   # Çıxılan
    print(descending-subtracted)

# Vurma
def multiplication():

    # Toplama funksiyası ilə eyni formada verilənləri bir sətir və boşluqlarla ayrılmış şəkildə qəbul edir
    list_of_multiplication= [float(num) for num in input("Enter the elements, separate with a space: ").split()]
    answer = 1 # Cavab

    # Hesablama dövrü
    '''
    Listin içindəki elementləri bir bir vuraraq answer dəyişənində saxlayır və sonda dövr bağlandıqda çap edir
    '''
    for i in list_of_multiplication:
        answer*=i
    print(answer)

# Bölmə
def division():
    dividend = float(input("Enter the dividend:")) # Bölünən
    divisor = float(input("Enter the dividor:"))   # Bölən
    print(dividend/divisor)

# Advanced calc funksiyaları

# Xətanın qarşısını alan funksiya
def evaluate_expression(expression):
    try:
        # Xəta olmadıqda cavabı hesablayır
        result = eval(expression)
        return result
    except ZeroDivisionError:  # 0-a bölünmə xətası
        return "Error: Division by zero!"
    except Exception as e:     # Səhv daxil edilmiş ifadə və digər xətalar
        return 'Please enter correct expression, not another strings'

# Advanced calc'ın əsasını təşkil edən hesablama funksiyası
def advanced_calculator(expression):
        '''
        Xətanı yoxlamaq üçün funksiya çağırır və cavabı ekrana yazdırır
        '''
        result = evaluate_expression(expression)
        print(f"Result: {result}")

# Əsas dövr
while True:

    # Məlumat kitabçası
    print("""
          What do you need?:
          -Simple calculator for only one operation = s
          -Advanced calculator for expressions  = a
          -If you want close the program write 'quit'
          """)
    value = input(":")  # Növü seçmək və ya proqramı bağlamaq üçün input
    
    # Simple calc 
    if value == 's':
        print("""
                      -Simple calc-
              Enter the operation like(+,-,,/)
              If you want to close the simple calc, write 'quit'
              """)
        
        # Simple calc'ın dövrü
        while True:
            value = input("Enter the operation:")  # Əməliyyatı təyin etmək və ya proqramı bağlamaq üçün input
            if value == '+':
                addition()
            elif value == '-':
                subtraction()
            elif value == '*':
                multiplication()
            elif value == '/':
                division()
            elif value == 'quit':
                print("Simple calc closed")
                break
            else:    # Dəyər doğru daxil edilmədikdə
                print("Please,enter a value according to the instructions ")
                
    # Advanced calc
    elif value == 'a':
        print("""
                      -Advanced calc-
              Enter the expression like(10+5*3-20/4)
              If you want to close advanced calc, write 'quit'
              """)
        
        # Advanced calc'ın dövrü
        while True:
            value = input("Enter expression:")
            if value == 'quit':
                break
            else:
                advanced_calculator(value)
    elif value == 'quit':
        break
    else:   # Dəyər doğru daxil edilmədikdə
        print("Please,enter a value according to the instructions ")