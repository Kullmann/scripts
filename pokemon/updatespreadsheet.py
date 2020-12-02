from getcardvalue import *
import pygsheets
gc = pygsheets.authorize()

sh = gc.open('Pokemon_Cards')
wk1 = sh[0]

cardNames = wk1.get_col(3)
fullCardDesc = []

cardNames.pop(0)  # Get rid of card name identifier
for card in cardNames:
    if card != "":
        fullCardDesc.append(card)

setNames = wk1.get_col(4)
setNames.pop(0)
for i in range(0, len(fullCardDesc)):
    fullCardDesc[i] += " " + setNames[i]

isHolo = wk1.get_col(5)
isHolo.pop(0)
for i in range(0, len(fullCardDesc)):
    if isHolo[i] == "Y":
        fullCardDesc[i] += " " + "holo"
    else:
        fullCardDesc[i] += " " + "non-holo"
    print(fullCardDesc[i])

counter = 2
values = wk1.get_col(6)
values.pop(0)
for i in range(0, len(fullCardDesc)):
    cardValue = pokemonValueMavin(fullCardDesc[i])
    time.sleep(3)
    if values[i] != cardValue:
        wk1.update_value("F" + str(counter), cardValue)
    counter += 1
exitBrowser()

updatePageNum = False
if updatePageNum:
    cardNumbers = wk1.get_col(1)
    cardNumbers.pop(0)
    counter = 1
    rowNum = 2
    for number in cardNumbers:
        wk1.update_value("B" + str(rowNum), "Page " + str(counter))
        rowNum += 1
        if int(number) % 9 == 0:
            counter += 1
        if counter == 99:
            time.sleep(110)
