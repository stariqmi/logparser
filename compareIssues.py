import xlrd


class compareKnownissues():
	def __init__(self, founderrors, knownerrorspath):

		 

		self.founderrors = founderrors
		self.knownerrorspath = knownerrorspath


	def compare(self):
		if not self.founderrors:
			return 0

		workbook = xlrd.open_workbook(self.knownerrorspath)
		sheet = workbook.sheet_by_index(0)
		data = [sheet.cell_value(row, 0)for row in range(sheet.nrows)]

		data = [str(i) for i in data]
		data = [i.lower() for i in data]
		if (set(data) & set(self.founderrors) and (len((set(data) & set(self.founderrors))) == len(self.founderrors))):
			print 'Possible known errors found in the logs, the keywords matching are: ' + ', '.join(set(data) & set(self.founderrors))
			return 1
		else:
				if(set(data) & set(self.founderrors)):
					print 'The following known errors were found, the keywords matching are: '  + ', '.join(set(data) & set(self.founderrors)) + ' \nBut possible new errors are also found: ' + ', '.join(x for x in set(self.founderrors) if x not in set(data))
					return 2
				else:
					print 'No known errors found, but possible new errors found in the logs, the errors are: ' + ', '.join(set(self.founderrors))
					return set(self.founderrors)


ins = open( "C:\Users\I841363\Desktop\\test.txt", "rU" )
array = []
for line in ins:
	line = line.replace("\n", "")
    	array.append( line )
ins.close()


x = compareKnownissues(array, 'C:\Users\I841363\Desktop\\testinput.xlsx')
y = x.compare()
print y

