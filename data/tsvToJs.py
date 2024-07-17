# CONSTANTS
inputFile = "data.tsv" # make it a tsv file
outputFile = "data.js" # make it a js file
numHeaderRows = 1 # rows that are like column names but not actual data for the QUIZ


import csv, json

listOfRows = []
with open(inputFile) as tsvFile:
    tsvReader = csv.reader(tsvFile, delimiter="\t", quotechar='"')
    rowIndex = 0
    for row in tsvReader:
        # skip header rows at top
        if rowIndex < numHeaderRows:
            rowIndex += 1
            continue
        
        # Make sure all rows have only 2 items
        if len(row) != 2:
            print("WARNING: THE ROW BELOW DOES NOT HAVE EXACTLY 2 ITEMS - ENDING LOOP:")
            print(row)
            break

        person, content = row
        listOfRows.append(row)

    # dump data as js variable into file
    with open(outputFile, "w+") as jsFile:
        jsFile.write("const DATA = \n" + json.dumps(listOfRows))


        
