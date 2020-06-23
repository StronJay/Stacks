class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            previousMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(previousMinMax["min"], number)
            newMinMax["max"] = max(previousMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

mms = MinMaxStack()
mms.push(5)
mms.push(4)
mms.push(8)
mms.push(33)
mms.push(324)
mms.push(34)
mms.push(42)
print(mms.peek())
print(mms.getMin())
print(mms.getMax())
mms.pop()
print(mms.peek())