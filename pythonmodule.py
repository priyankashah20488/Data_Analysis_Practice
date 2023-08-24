#simple print

print("Hello")

#check the module name
print(__name__)

#importing another module
import calculator

print(dir(calculator))

print(calculator.__name__)

print(calculator.add.__doc__)

r = calculator.add(34,45,12,3,5,23)
print(r)

from calculator import add
print(add(23,34,34,34))

from calculator import add as summetion
print(summetion(23,34,34,34))

