import sys
import os
import subprocess as sp
from htmlx import html, body, h1
print(html(body(h1('Hello, World!'))))
dir_path = os.path.dirname(os.path.realpath(__file__))

cwd = os.getcwd()

activeDir = ''.join([cwd, "\\"])
print("Active directory: ", activeDir)

jsPath = ''.join([activeDir, 'js'])
cssPath = ''.join([activeDir, 'css'])

checkPaths = [jsPath, cssPath]

for path in checkPaths:
    if not os.path.exists(path):
        os.makedirs(path)

def createFile(location, data):
    version = sys.version
    with open(location, "wb") as createdFile:
        if(version.startswith('2.')):
            createdFile.write(data)
        elif(version.startswith('3.')):
            createdFile.write(bytes(data, "UTF-8"))
        
#index.html
filename = "index.html"
fullPath = ''.join([activeDir, filename])

#html parts
pageStart = "<!DOCTYPE html>\n<html lang='en'>"
headStart = "\n\t<head>"
title = "\n\t\t<title>Title</title>"
headLink = "\n\t\t<link rel='stylesheet' href='css/styles.css' />"
headEnd = "\n\t</head>"
bodyStart = "\n\t<body>"
testDiv = "\n\t\t<div ng-controller='MainCtrl as ctrl'><h1>{{ctrl.greeting}}</h1></div>"
btn = "\n\t\t<button onclick=\"alertMe()\">Alert Me(5 * 5 = {{5*5}})!</button>"
myJs = "\n\t\t<script src=\"js/scripts.js\"></script>"
ang = "\n\t\t<script src=\"https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js\"></script>"
bodyEnd = "\n\t</body>"
pageEnd = "\n</html>"

htmlFile = ''.join([pageStart, headStart, title, headLink, headEnd, bodyStart, testDiv, btn, ang, myJs, bodyEnd, pageEnd])

createFile(fullPath, htmlFile)

#scripts.js File
scriptsjs = "scripts.js"
jsFullPath = ''.join([activeDir, "js/", scriptsjs])
jsOne = "function alertMe(){ alert('ME!'); }"
angAppStart = "\n(function(){"
angModule = "\n\tangular.module('MainApp', [])"
angControllerStart = "\n\t.controller('MainCtrl', function(){"
angthis = "\n\t\tvar ctrl = this;"
angGreeting = "\n\t\tctrl.greeting = 'Hello, from Angular!'"
angControllerEnd = "\n\t});"
angAppEnd = "\n})();"

jsScriptsFile = ''.join([jsOne, angAppStart, angModule, angControllerStart, angthis, angGreeting, angControllerEnd, angAppEnd])

createFile(jsFullPath, jsScriptsFile)

#styles.css
stylescss = "styles.css"
stylesFullPath = ''.join([activeDir, "css/", stylescss])
baseCss = "body { text-align: center;background-color: rgb(240,240,150); }"

stylesFile = ''.join([baseCss])

createFile(stylesFullPath, stylesFile)

# Uncomment to open project folder in Visual Studio Code, or replace with editor of your choice
# np = 'code'
# cmdLine = ' '.join([np, activeDir])
# os.system(cmdLine)