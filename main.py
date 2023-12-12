from math_operation import basic_operation,power_operation,apply_operation

# Test basic_operations
result_basic = basic_operation(10, 5)
print("Basic Operations Result:", result_basic)

# Test power_operation
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)

# Test power_operation with modulo
result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

# Test apply_operations
operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operation(operations)
print("Apply Operations Result:", result_apply)
Updated at Tue Dec 12 15:24:04 2023
Updated at Tue Dec 12 16:10:55 2023
Updated at Tue Dec 12 16:25:35 2023
Updated at Tue Dec 12 16:53:29 2023