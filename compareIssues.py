import xlrd
import sys
import re

class compareKnownissues():
	def __init__(self, founderrors, knownerrorspath):
		self.founderrors = founderrors
		self.knownerrorspath = knownerrorspath
	def compare(self):
		workbook = xlrd.open_workbook(Known_Install_log_Issues)
		sheet = workbook.sheet_by_index(0)
		data = [sheet.cell_value(row, 0)for row in range(sheet.nrows)]
		#Filepaths changed between Windows and Mac computers
		knownerrorsTXT = open('C:\Users\I841251\Desktop\logparser\KnownErrors.txt', 'w')
		unknownerrorsTXT = open('C:\Users\I841251\Desktop\logparser\UnknownErrors.txt', 'w')

		for line in ErrorArray :
			if line in set(data) :
				knownerrorsTXT.truncate()
				knownerrorsTXT.write(line)
				knownerrorsTXT.write("\n")
			else:
				unknownerrorsTXT.truncate()
				unknownerrorsTXT.write(line)
				unknownerrorsTXT.write("\n")
		knownerrorsTXT.close()
		unknownerrorsTXT.close()

#On Windows, it's easier to use input as opposed to raw_input on Mac
setupengine = input('Please input the filepath of a setupengine.log file: ')
Known_Install_log_Issues = input('Please input the filepath of Known_Install_log_Issues_.xlsx: ')

ErrorArray = []

with open(setupengine, 'r') as lines:
	lines = lines.readlines()
	for line in lines:
		if re.match("(.*)(E|e)rror:(.*)", line):
			ErrorArray.append(line)
		#	ErrorArray.append("\n")
		else:
			pass

x = compareKnownissues(ErrorArray, Known_Install_log_Issues)
y = x.compare()
print y
print ErrorArray

#Absolute paths on Risa's home computer (Mac)
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/setupengineKnownErrors.log
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/setupengineUnknownErrors.log
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/Known_Install_log_Issues_.xlsx

#Absolute paths on Risa's work computer (Windows)
#"C:\Users\I841251\Desktop\logparser\setupengineKnownErrors.log"
#"C:\Users\I841251\Desktop\logparser\setupengineUnknownErrors.log"
#'C:\Users\I841251\Desktop\logparser\Known_Install_log_Issues_.xlsx'