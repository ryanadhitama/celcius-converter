print("-----------------------")
print("-- Celcius Converter --")
print("-----------------------")

def celciusToReamur(celcius) :
    toReamur = 4 / 5 * float(celcius)
    printReamur = "Celcius to Reamur is "+str(toReamur)
    return toReamur, printReamur

def celciusToFahrenheit(celcius) :
    toFahrenheit = (9 / 5 * float(celcius)) + 32
    printFahrenheit = "Celcius to Fahrenheit is "+str(toFahrenheit)
    return toFahrenheit, printFahrenheit

def celciusToKelvin(celcius) :
    toKelvin = 273 + float(celcius)
    printKelvin = "Celcius to Kelvin is "+str(toKelvin)
    return toKelvin, printKelvin


celcius = input("Please input celcius temperature : ")

reamur, printReamur = celciusToReamur(celcius)
fahrenheit, printFahrenheit = celciusToFahrenheit(celcius)
kelvin, printKelvin = celciusToKelvin(celcius)

print("Results : ")
print(printReamur)
print(printFahrenheit)
print(printKelvin)
