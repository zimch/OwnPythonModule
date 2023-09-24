from my_module import find_args
from my_module.math_module import MathHelper

def app():
    helper = MathHelper()
    args = find_args()
    
    if len(args.numbers) != 2: 
        print("Только 2 числа")
        return
    
    try:
        match args.operation:
            case '+':
                print(helper.plus(args.numbers[0], args.numbers[1]))
            case '-':
                print(helper.minus(args.numbers[0], args.numbers[1]))
            case '*':
                print(helper.multiply(args.numbers[0], args.numbers[1]))
            case '/':
                print(helper.division(args.numbers[0], args.numbers[1]))
            case _:
                print("Нет такой операции")
                
    except:
        print("Что-то не так :(")
        