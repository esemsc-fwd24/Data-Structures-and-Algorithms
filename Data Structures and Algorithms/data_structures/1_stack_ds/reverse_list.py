# Use the Stack class to return the reverse of a string
from stack_ds.stacks import Stack


def reverse_string(string):
    stack = Stack()
    [stack.push(char) for char in string]
    return "".join([stack.pop() for i in range(stack.size())])


print(reverse_string("abcdefgh"))
