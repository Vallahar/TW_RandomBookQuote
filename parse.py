# -*- coding: utf-8 -*-
import os

def writeFile(start, end, fileName):
    os.chdir("/sources")
    textToWrite = ""
    charIndex = start
    while charIndex < end:
        textToWrite += content[charIndex]
        charIndex += 1

    file = open(fileName, "w")
    file.write(textToWrite)
    file.close()

# Retrieve the source text as a string
sourceFile = open("sources/source.txt")
content = sourceFile.read()
content = content.replace("--", "-")
sourceFile.close()

# Define separator substrings
introTitle = "-/INTRODUCCIÓN"
poemsTitle = "-/RIMAS"
legendsTitle = "-/LEYENDAS"
lettersTitle = "-/CARTAS LITERARIAS"

# Parse Introduction
introStart = content.find(introTitle) + len(introTitle) + 1
introEnd = content.find(legendsTitle)

totalChars = introEnd - introStart
print("Intro start at: %i" % introStart)
print("Intro end at: %i" % introEnd)
print("Total characters = %i" % totalChars)
print("'''''''''''")

writeFile(introStart, introEnd, "intro.txt")

# Parse Legends
legendStart = content.find(legendsTitle) + len(legendsTitle) + 1
legendEnd = content.find(lettersTitle)

totalChars = legendEnd - legendStart
print("Legends start at: %i" % legendStart)
print("Legends end at: %i" % legendEnd)
print("Total characters = %i" % totalChars)
print("'''''''''''")

writeFile(legendStart, legendEnd, "legends.txt")

# Parse Letters
letterStart = content.find(lettersTitle) + len(lettersTitle) + 1
letterEnd = content.find(poemsTitle)

totalChars = introEnd - introStart
print("Letters start at: %i" % letterStart)
print("Letters end at: %i" % letterEnd)
print("Total characters = %i" % totalChars)
print("'''''''''''")

writeFile(letterStart, letterEnd, "letters.txt")

# Parse Poems

poemStart = content.find(poemsTitle) + len(poemsTitle) + 1
poemEnd = content.find("FIN")
totalChars = poemEnd - poemStart

print("Poems start at: %i" % poemStart)
print("Poems end at: %i" % poemEnd)
print("Total characters = %i" % totalChars)

writeFile(poemStart, poemEnd, "poems.txt")
