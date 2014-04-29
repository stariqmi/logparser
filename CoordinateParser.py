from datetime import datetime

# Processor Class
class Processor(object):
	def __init__(self, lines):
		self.lines = lines

		# Constants
		self.indicator = "Processing coordinate"
		self.seq1_end = "No other setup engine running under the same installiverse id.  Continuing..."
		self.seq2_end = "*** FEATURE TREE DUMP ***"
		self.seq3_end = "** UNCACHING DUs..."

	def findPoint(self, line):
		if (self.indicator in line) or (self.seq1_end in line) or (self.seq2_end in line) or (self.seq3_end in line):
			return True
		else:
			return False

	def parse(self):
		points = []
		for line in self.lines:
			if self.findPoint(line):
				points.append(line)

		coord_csv = open("coordinates.csv","w")
		coord_csv.write("Seconds,Coordinate\n")
		x = 0
		fmt = '%Y-%m-%d %H:%M:%S'

		for i in range(0,len(self.lines)):
			if self.indicator in self.lines[i]:
				a = datetime.strptime("2010-01-01 " + self.lines[i].split()[0][:-4], fmt)
				b = datetime.strptime("2010-01-01 " + self.lines[i+1].split()[0][:-4], fmt)
				coord_csv.write(str((b-a).seconds) + "," + self.lines[i].split(": ")[1].strip().replace(",",".") + "\n")
		