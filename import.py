import importlib

module_name = 'math'
math = importlib.import_module(module_name)

result = math.sqrt(int(input('Enter an integer : ')))
print(result)  


