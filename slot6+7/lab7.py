from Question1 import arrayStack
from  Question1 import decimalToBinary

stack_str = arrayStack()

print("Is stack empty?", stack_str.isEmpty() )

n = int(input("Enter the number of element "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    stack_str.push(element)

print("Stack after push: ")
stack_str.traverse()

print("Is stack empty?", stack_str.isEmpty() )

print("The element is pop: ",stack_str.pop())
print("Stack after pop: ")
stack_str.traverse()

print("The top element: ", stack_str.top())

stack_str.clear()
print("Stack after clear: ")
stack_str.traverse()

while True:
    decimal_number = input("Enter a decimal number: ")
    if decimal_number.isdecimal():
        break
    else:
        print("Please enter a decimal number!")

binary_number = decimalToBinary(decimal_number)
print(f"The binary number of {decimal_number} is {binary_number}")

print()
print()

from Lab2_Q2 import Queue
from Lab2_Q2 import convert_real_number

queue_str = Queue()
print("Is queue empty? ", queue_str.isEmpty())

n = int(input("Enter the number of element "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    queue_str.enqueue(element)

print("Queue after enqueue: ")
queue_str.traverse()

print("Is queue empty? ", queue_str.isEmpty())

queue_str.dequeue()
print("Queue after dequeue 1 time: ")
queue_str.traverse()

print("First element: ", queue_str.first())

print("Clear queue")
queue_str.clear()
print("Is queue empty? ", queue_str.isEmpty())

number = float(input("Enter a real number in range [0; 1): "))
result = convert_real_number(number)
print("The binary number of that number is ")
result.traverse()


