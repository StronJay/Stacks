test1 = "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash/../../../../../.."
test2 = "../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../.."
test3 = "/foo/./././bar/./baz///////////test/../../../ppa"
def shortestPath(string):
    isRootDirectory = string[0] == "/"
    tokens = filter(isImportantToken, string.split("/"))
    print(tokens)
    stack = []
    if isRootDirectory:
        stack.append("")
    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)


def isImportantToken(token):
    print(token)
    return len(token) > 0 and token != "."

print(shortestPath(test3))
tort = ["jdf"]
print(" thisIs weird ".join(tort))
string = "withoutatheakeyayouacouldagetalosta"
list = string.split('a')
print(list)