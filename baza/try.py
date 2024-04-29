try:
    num1 = int(input("Введите число: "))
except:
    print("Ошибка")
    
    
    
try:
    num1 = int(input("Введите число: "))
except Exception as error:
    print(error)
    
    
while True:
    try:
        num1 = int(input("Введите число: "))
        num2 = int(input("Введите число: "))
        print(num1 / num2)
        break
    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except Exception as e:
        print("Ошибка")
    finally:
        print("Конец итеррации")
        
