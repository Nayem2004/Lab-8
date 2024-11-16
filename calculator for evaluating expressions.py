#Calculator for Evaluating Mathematical Expressions

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


def evaluate_expression(expression):
    
    # Creates stacks for numbers and operators
    num_stack = Stack()
    op_stack = Stack()

    # Defines precedence of operators.
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Helper function to apply an operator.
    def apply_operator():
        # Pop operator and two numbers, apply the operator, and pushes the result.
        operator = op_stack.pop()
        right = num_stack.pop()
        left = num_stack.pop()
        if operator == '+':
            num_stack.push(left + right)
        elif operator == '-':
            num_stack.push(left - right)
        elif operator == '*':
            num_stack.push(left * right)
        elif operator == '/':
            num_stack.push(left / right)

    i = 0  # Index to iterate through the expression.
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            # Ignores whitespace.
            i += 1
            continue

        if char.isdigit():
            # Parses the entire number (multi-digit support)
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num_stack.push(num)  # Pushes the parsed number onto the stack.
            continue

        if char == '(':
            # Pushes opening parenthesis onto the operator stack.
            op_stack.push(char)

        elif char == ')':
            # Processes all operators until a '(' is encountered.
            while not op_stack.is_empty() and op_stack.peek() != '(':
                apply_operator()
            op_stack.pop()  # Discards the '('

        elif char in precedence:
            # Processes operators with higher or equal precedence.
            while (not op_stack.is_empty() and
                   op_stack.peek() != '(' and
                   precedence[op_stack.peek()] >= precedence[char]):
                apply_operator()
            op_stack.push(char)  # Pushes the current operator onto the stack.

        i += 1

    # Applies remaining operators in the operator stack.
    while not op_stack.is_empty():
        apply_operator()

    # The final result is the only number in the number stack.
    return num_stack.pop()


def main():
    # Test cases to validate the program.
    expression1 = "(((6+9)/3)*(6-4))"  # Balanced and evaluatable
    expression2 = "10 + (2 * (6 + 4))"  # Nested parentheses
    expression3 = "100 * (2 + 12) / 4"  # Simple expression with precedence

    # Prints results for each test case.
    print(evaluate_expression(expression1))  # Expected: 10
    print(evaluate_expression(expression2))  # Expected: 30
    print(evaluate_expression(expression3))  # Expected: 350


# Executes the program.
main()
