def basic_operation(a,b):
    try:
        addition = a+b
        substraction = a-b
        multiple = a*b
        division = a/b
        return {"Addition": addition ,"Substraction" : substraction,"Multiplication":multiple,"Division":division }
    except ZeroDivisionError:
        return {"Error: Division by zero"}       
#print(basic_operation(9,8))
"""def power_operation (base, exponent , **kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo_val= kwargs['modulo']
            result = result % modulo_val
        return result
    except Exception as e:
    #return f"Error: {e}"
        print("Error")"""
def power_operation (base, exponent , **kwargs):
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo_val= kwargs['modulo']
            result = result % modulo_val
        return result

def apply_operation(operation_list):
    results = list(map(lambda x:x[0](*x[1]),operation_list))
    return results

Updated at Tue Dec 12 16:10:55 2023
Updated at Tue Dec 12 16:25:35 2023
Updated at Tue Dec 12 16:53:29 2023