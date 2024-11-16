#Balanced Parentheses Checker

class Stack:
    def __init__(self):
        # Initializes an empty list to act as the stack.
        self.items = []

    def is_empty(self):
        # Checks if the stack is empty.
        return len(self.items) == 0

    def push(self, item):
        # Adds an item to the stack.
        self.items.append(item)

    def pop(self):
        # Removes and returns the top item of the stack, or None if empty.
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        # Returns the top item of the stack without removing it, or None if empty.
        return self.items[-1] if not self.is_empty() else None


def is_balanced(expression):
    
    # Creates a stack to track opening parentheses.
    stack = Stack()

    # Defines the matching pairs for parentheses.
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # If the character is an opening parenthesis, then it pushes it onto the stack.
        if char in opening:
            stack.push(char)
        elif char in closing:
            # If it's a closing parenthesis, it checks for a match.
            # If the stack is empty or the top of the stack does not match, it returns False.
            if stack.is_empty() or stack.pop() != matches[char]:
                return False

    # If the stack is empty at the end, then the parentheses are balanced.
    return stack.is_empty()


def main():
    # Tests cases to check different scenarios
    expression1 = "({X+Y}*Z)"    # Balanced
    expression2 = "{X+Y}*Z)"     # Unbalanced (extra closing parenthesis)
    expression3 = "({X+Y}*Z"     # Unbalanced (missing closing parenthesis)
    expression4 = "[A+B]*({X+Y}]*Z)"  # Unbalanced (mismatched parenthesis)

    # Prints results for each test case.
    print(is_balanced(expression1))  # Expected: True
    print(is_balanced(expression2))  # Expected: False
    print(is_balanced(expression3))  # Expected: False
    print(is_balanced(expression4))  # Expected: False


# Executes the program.
main()
