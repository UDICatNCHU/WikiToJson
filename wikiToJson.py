# -*- coding: utf-8 -*-

import sys
import os
import json

filedir = sys.argv[1]
output = sys.argv[2]
outputFile = open( output, 'w',encoding = 'UTF-8')

j = {}

def textDeal(filename , first):
	file = open(filename,'r')
	contentExtract = bool(0)
	content = ""
	contentTitle = ""
	contentId = ""
	contentUrl = ""
	
	for sentence in file.readlines():
		if sentence!='\n':
			#print sentence + "\n"
			if sentence.find("<doc id=\"") != -1:
				#print(sentence)
				be = sentence.find("id=\"") + 4
				en =  sentence.index("\"" , be)
				contentId = sentence[be:en] 
				
				be = sentence.find("url=\"") + 5
				en =  sentence.index("\"" , be)
				contentUrl = sentence[be:en] 


				be = sentence.find("title=\"") + 7
				en =  sentence.index("\"" , be)
				contentTitle =  sentence[be:en] 
				contentExtract = bool(1)
			elif contentExtract:
				if("</doc>" in sentence):
					contentExtract = bool(0)
					if first == 1:
						print("first", end='')
						first = 0 
					else:
						outputFile.write(",")
						#print(",")
					c = { "id":int(contentId) , "url":contentUrl , "title":contentTitle , "content":content }
					#print(contentTitle)
					jsonString = json.dumps( c , ensure_ascii=False)
					outputFile.write(jsonString)
					content = ""
				else:
					content += sentence
outputFile.write("[")
print("[" , end='')
first = 1
for root, dirs, files in os.walk(filedir):
	#print root
	for f in files:
		#print os.path.join(root, f)

		filepath = os.path.join(root, f)
		#print (filepath)
		if(first == 1):
			textDeal(filepath , 1)
			first = 0
		else:
			textDeal(filepath , 0)
outputFile.write("]")
print("]", end='')
outputFile.close





