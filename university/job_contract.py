def spaceDeleter(textClone):  # deletes any number of space from the end of string
    for i in range(len(textClone) - 1, 0, -1):
        if textClone[i] == ' ':
            textClone = textClone[:-1]
        else:
            return textClone


def tab():
    global text

    #  control switches
    isInSingleLine = True
    doesIfWhileForContainBracket = True
    isAfterIfForWhile = False
    isTwoPartOperatorSuspicious = False
    isIncludeStatement = False
    isToBeCopied = False
    isAfterOpenBraceOrBracket = False
    canBeThereElse = False
    isSuspiciousOperator = False
    isAssignmentPhrase = False
    textClone = ""
    foundNotOprator = False
    isAddressOperator = False
    tabs = 0
    bracesDepth = 0
    bracketsDepth = 0
    specialChars = ['\n', '\t']
    operatorSigns = ['=', '<', '>', '+', '-', '*', '/', '%', '!', '&', '|']

    for char in range(len(text)):  # checks char by char

        if text[char] == '\"':
            textClone += '\"'
            if isToBeCopied:
                if isIncludeStatement:
                    textClone += '\n'
                    isIncludeStatement = False
                isToBeCopied = False
            else:
                isToBeCopied = True

        elif isToBeCopied:
            if text[char] not in specialChars:
                textClone += text[char]
            else:
                if text[char] == '\n':
                    textClone += '\\n'
                elif text[char] == '\t':
                    textClone += '\\t'

        elif text[char] == '#':
            isIncludeStatement = True
            textClone += '#'

        elif text[char] == '{':
            doesIfWhileForContainBracket = True
            isAfterOpenBraceOrBracket = True
            tabs += 1
            if isAssignmentPhrase:
                textClone += '{'

            else:
                textClone += '{\n' + tabs * '\t'

        elif text[char] == '}':
            canBeThereElse = True
            textClone = spaceDeleter(textClone)
            tabs -= 1
            if isAssignmentPhrase:
                textClone += '}'

            else:
                textClone = textClone[:-1]
                textClone += '}\n' + tabs * '\t'

        elif text[char] == '(':
            bracesDepth += 1
            isAddressOperator = False
            isAfterOpenBraceOrBracket = True
            isTwoPartOperatorSuspicious = False
            textClone += '('

        elif text[char] == ')':
            bracesDepth -= 1
            isAssignmentPhrase = False
            isInSingleLine = False
            if isAfterIfForWhile:
                doesIfWhileForContainBracket = False
                isAfterIfForWhile = False
            textClone = spaceDeleter(textClone) + ')'

        elif text[char] == '[':
            isAfterOpenBraceOrBracket = True
            textClone += '['

        elif text[char] == ']':
            textClone = spaceDeleter(textClone) + ']'

        elif text[char] == ';':
            isAssignmentPhrase = False
            isInSingleLine = False
            textClone = spaceDeleter(textClone)
            if isAfterIfForWhile or bracesDepth != 0:
                textClone += '; '
            else:
                textClone += ';\n' + tabs * '\t'

        elif text[char] == '>':
            isAfterOpenBraceOrBracket = False

            if isIncludeStatement:
                textClone += '>\n'
                isIncludeStatement = False
            elif textClone[-2] == '>':
                textClone = textClone[:-1]
                textClone += '> '
            elif textClone[-1] == ' ':
                textClone += '> '
            else:
                textClone += ' > '

        elif text[char] == '+':
            if isSuspiciousOperator:  # found second +
                textClone = textClone[:-1]  # deletes last space because it should be like ++
                textClone += '+'
                if textClone[-4] != ';' and textClone[-4] != '\n':
                    textClone = textClone[:-3] + '++'
                isSuspiciousOperator = False
                isTwoPartOperatorSuspicious = False

            else:
                isSuspiciousOperator = True
                isTwoPartOperatorSuspicious = True

                if textClone[-1] == ' ':
                    textClone += '+ '
                else:
                    textClone += ' + '

        elif text[char] == '-':
            if isSuspiciousOperator:  # found second -
                textClone = textClone[:-1]  # deletes last space because it should be like --
                textClone += '-'
                if textClone[-4] != ';' and textClone[-4] != '\n':
                    textClone = textClone[:-3] + '--'
                isSuspiciousOperator = False
                isTwoPartOperatorSuspicious = False

            else:
                isSuspiciousOperator = True
                isTwoPartOperatorSuspicious = True

                if textClone[-1] == ' ':
                    textClone += '- '
                else:
                    textClone += ' - '

        elif text[char] in operatorSigns:
            isAfterOpenBraceOrBracket = False
            if text[char] == '!':
                foundNotOprator = True
                if textClone[:-1] == ' ':
                    textClone += '!'
                else:
                    textClone += ' !'
                isTwoPartOperatorSuspicious = True
                continue

            elif text[char] == '&':
                if isAddressOperator:
                    textClone += '& '
                    isAddressOperator = False
                    continue

                else:
                    isAddressOperator = True
                    if textClone[-1] == ' ':
                        textClone += '&'
                    else:
                        textClone += ' &'
                    continue

            elif text[char] == '=':
                isAssignmentPhrase = True
                if foundNotOprator and isTwoPartOperatorSuspicious:
                    textClone += '= '
                    isTwoPartOperatorSuspicious = False
                    foundNotOprator = False
                    continue

            if isIncludeStatement:
                textClone += text[char]
                continue

            if isTwoPartOperatorSuspicious:
                textClone = textClone[:-1]
                textClone += text[char]
                isTwoPartOperatorSuspicious = False

            else:
                isTwoPartOperatorSuspicious = True

                if textClone[-1] == ' ':
                    textClone += text[char]
                else:
                    textClone += ' ' + text[char]

            textClone += ' '

        elif text[char] == ' ':
            if textClone[-1] != ' ' and isInSingleLine and not isAfterOpenBraceOrBracket and textClone[-2:] != 'if' \
                    and textClone[-3:] != 'for' and textClone[-5:] != 'while' and textClone[-1] != '\t':
                textClone += ' '

        elif text[char] == ',':
            isAfterOpenBraceOrBracket = False
            textClone = spaceDeleter(textClone) + ', '

        elif text[char] == '\n':
            if textClone[-4:] == 'else':
                textClone += '\n' + tabs * '\t'

        elif text[char] not in specialChars:
            isAddressOperator = False
            foundNotOprator = False
            isTwoPartOperatorSuspicious = False
            isAfterOpenBraceOrBracket = False
            isInSingleLine = True
            isSuspiciousOperator = False

            if isIncludeStatement:
                textClone += text[char]
                continue

            if canBeThereElse:
                canBeThereElse = False
                if text[char:char + 4] == 'else':
                    textClone = textClone[:-tabs - 1]

            if not doesIfWhileForContainBracket and bracesDepth == 0:
                textClone += '\n' + tabs * '\t' + text[char]
                doesIfWhileForContainBracket = True

            else:
                textClone += text[char]
                if text[char] == 'i' and text[char:char + 2] == 'if':
                    isAfterIfForWhile = True

                elif text[char] == 'f' and text[char:char + 3] == 'for':
                    isAfterIfForWhile = True

                elif text[char] == 'w' and text[char:char + 5] == 'while':
                    isAfterIfForWhile = True

    text = textClone
    print(textClone)


global text  # holds the input


def find_main(lines):  # if the main function is seen
    started = False
    need_to_check = False
    to_check = "main"
    ignore = [' ', '\n', '\t']
    source = '\n'.join(lines)
    indx = 3
    for i in range(len(source)):
        if indx == -1:
            if source[-i - 1] not in ignore:
                return False

            return True

        if source[-i - 1] == '(':
            need_to_check = True
            continue

        if need_to_check:
            if source[-i - 1] == to_check[indx]:
                indx -= 1
                started = True
                continue

            if source[-i - 1] not in ignore or started and source[-i - 1] in ignore:
                return False

    if indx == -1:
        return True

    return False


def get_source():  # gets the source from the user and check if it is complete or not
    function_declaration = False
    reached_main = False
    brackets_depth = 0
    functions = 1
    lines = []
    while not reached_main or functions:
        lines.append(input())
        for i in lines[-1]:
            if i == '(':
                if brackets_depth == 0 and find_main(lines):
                    reached_main = True

                if brackets_depth == 0:
                    function_declaration = True

            elif i == '{':
                start = False
                function_declaration = False
                brackets_depth += 1

            elif i == '}':
                brackets_depth -= 1
                if brackets_depth == 0 and reached_main:
                    functions -= 1

            elif i == ';':
                if function_declaration:
                    functions += 1
                    function_declaration = False

    return '\n'.join(lines)




text = get_source()
tab()
