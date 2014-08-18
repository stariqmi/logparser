import xlrd
import sys

class compareKnownissues():
	def __init__(self, founderrors, knownerrorspath):
		self.founderrors = founderrors
		self.knownerrorspath = knownerrorspath
	def compare(self):
		workbook = xlrd.open_workbook(Known_Install_log_Issues)
		sheet = workbook.sheet_by_index(0)
		data = [sheet.cell_value(row, 0)for row in range(sheet.nrows)]
		knownerrorsTXT = open('/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser//KnownErrors.txt', 'w')
		unknownerrorsTXT = open('/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser//UnknownErrors.txt', 'w')

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
		
setupengine = raw_input('Please input the filepath of a setupengine.log file: ')
Known_Install_log_Issues = raw_input('Please input the filepath of Known_Install_log_Issues_.xlsx: ')

ErrorArray = []
with open(setupengine) as lines:
	lines = lines.readlines()
	for line in lines:
		if 'error:' in line:
			ErrorArray.append(line)
		else:
			pass

x = compareKnownissues(ErrorArray, Known_Install_log_Issues)
y = x.compare()
print y
print ErrorArray

#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/setupengineKnownErrors.log
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/setupengineUnknownErrors.log
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/Known_Install_log_Issues_.xlsx