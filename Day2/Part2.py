def add_opcode(inputopcodearray, decider):
    inputopcodearray[inputopcodearray[decider+3]] = inputopcodearray[inputopcodearray[decider+1]] + inputopcodearray[inputopcodearray[decider+2]]
    return inputopcodearray


def multiply_opcode(inputopcodearray, decider):
    inputopcodearray[inputopcodearray[decider+3]] = inputopcodearray[inputopcodearray[decider+1]] * inputopcodearray[inputopcodearray[decider+2]]
    return inputopcodearray


def opcode(inputopcodearray,decider):
    while decider < len(inputopcodearray):
        if inputopcodearray[decider] == 1:
            inputopcodearray = add_opcode(inputopcodearray,decider)
            decider += 4
        if inputopcodearray[decider] == 2:
            inputopcodearray = multiply_opcode(inputopcodearray,decider)
            decider += 4
        if inputopcodearray[decider] == 99:
            break;
    # print(inputopcodearray,decider)
    print(inputopcodearray)


# print(opcode(inputopcodearray,decider))

def verb_noun_finder():

    noun = 0
    verb = 0
    for noun in range (100):
        for verb in range(100):

            newArray = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 9, 19, 23, 2, 13, 23, 27, 1,
                        6, 27, 31, 2, 6, 31, 35, 2, 13, 35, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 9, 47, 51, 1, 51, 13,
                        55, 1, 55, 13, 59, 2, 59, 13, 63, 1, 63, 6, 67, 2, 6, 67, 71, 1, 5, 71, 75, 2, 6, 75, 79, 1, 5,
                        79, 83, 2, 83, 6, 87, 1, 5, 87, 91, 1, 6, 91, 95, 2, 95, 6, 99, 1, 5, 99, 103, 1, 6, 103, 107,
                        1, 107, 2, 111, 1, 111, 5, 0, 99, 2, 14, 0, 0]

            newArray[1] = noun
            newArray[2] = verb
            opcode(newArray,0)

            if newArray[0] == 19690720:
                print("Noun = ", noun)
                print("Verb = ", verb)
                res = 100*noun+verb
                print("Final answer = ", res)
                return res

            verb += 1
        noun += 1

print(verb_noun_finder())


