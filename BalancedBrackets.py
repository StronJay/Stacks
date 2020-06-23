test = "(((((({{{{{[[[[[([])]]]]]}}}}}))))))"
def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for bracket in string:
        print(stack)
        if bracket in openingBrackets:
            stack.append(bracket)
        elif bracket in closingBrackets:
            if not len(stack):
                return False
            elif stack[-1] == matchingBrackets[bracket]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(balancedBrackets(test))