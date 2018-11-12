def infoProcessor(inputText):
    # working with a temporary file allows easier manipulation of data
    tempf = open("DATATEXT.txt", "w+")
    tempf.write(inputText)
    tempf.close()
    tempf = open("DATATEXT.txt", "r")
    inputLINES = tempf.readlines()
    tempf.close()

    mealCardDATA = []

    # data stores all data in the form as a dictionary
    data = ["", ""]

    for inputLine in inputLINES:
        inputDATA = inputLine.split(' ')
        # print(inputDATA)

        for i in range(len(inputDATA)):
            if (inputDATA[i] == '\n'):
                pass
            elif (inputDATA[i][0].isdigit() or inputDATA[i][0] == '$'):
                data[0] = inputDATA[i]
                # print(inputDATA[i])
                # print(data["mealPrice"])
            else:
                data[1] += (inputDATA[i] + ' ')
                # print(inputDATA[i])
                # print(data["mealName"])
        if ((len(data[1]) == 0) or (len(data[0]) == 0)):
            pass
        else:
            mealCardDATA += data
            # print(mealCardDATA)
        # print(data["mealName"]); print(data["mealPrice"])

        data[0] = ""
        data[1] = ""

    return mealCardDATA
