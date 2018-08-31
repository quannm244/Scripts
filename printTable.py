# def printTable(list):

tableData = [['apples','oranges','cherries','banana','pineapple'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose'],
             ['test','holy']]
"""colWidth = [0] * len(tableData)
print(colWidth)
print(colWidth[0])"""

def checkMax(list):
    result={}
    row = 0
    for i in tableData:
        if row < len(i):
            row = len(i)
    result['row'] = row
    result['column']=len(tableData)

    return result

result = checkMax(tableData)
print(result)

"""for i in result:
        print(tableData[0][i]+tableData[1][i]+tableData[2][i])"""
