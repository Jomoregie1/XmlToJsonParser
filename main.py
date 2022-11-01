import xml.etree.ElementTree as ET
import json


def parseXmlAndConvertToJsonFile(xmlFile, outputFile):
    print(f'Parse this xml file: {xmlFile}')
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    abstractMethods = []
    parameters = []
    exceptions = []
    for abstractMethodElem in root.findall('abstract_method'):
        methodName = abstractMethodElem.attrib.get('name', '')
        visibility = abstractMethodElem.find('visibility').text
        paramElems = abstractMethodElem.find('arguments').findall('parameter')
        for elem in paramElems:
            dataType = elem.attrib.get('type')
            label = elem.text
            parameters.append(dict(dataType=dataType, label=label))
        arguments = dict(parameter=parameters)
        abstractMethod = dict(method_name=methodName, visibility=visibility, arguments=arguments)
        abstractMethods.append(abstractMethod)
        if abstractMethodElem.find('exceptions') is not None:
            exceptElems = abstractMethodElem.find('exceptions').findall('exception')
            for elem in exceptElems:
                exceptions.append(elem.text)
            abstractMethod['exceptions'] = dict(exception=exceptions)
        returnElem = abstractMethodElem.find('return')
        abstractMethod['return'] = returnElem.text
    resultDict = dict(abstract_method=abstractMethods)

    # Save to output file
    print(f'Json file is named here : {outputFile}')
    with open(outputFile, 'w') as f:
        json.dump(resultDict, f, indent=2)
    return resultDict


if __name__ == "__main__":
    result = parseXmlAndConvertToJsonFile(input('Please enter the inputFile file here: '),
                                          input('Please enter the name of the output file here: '))
