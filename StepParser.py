from datetime import datetime

class StepParser(object):
	def __init__(self, lines):
		self.steps = []
		self.lines = lines

		# Step times
		stepfile = open("steps.txt")
		for line in stepfile.readlines():
			self.steps.append(line.split(","))

	def parse(self):			

		# Step tracker
		tracker = 0
		started = False
		line_num = 0

		# Function variables referencing to instance variables
		steps = self.steps
		lines = self.lines

		# Loop through all the lines while trackers are left
		while tracker < len(steps):

			line = lines[line_num]

			# If step starting point is same as previous step's ending point
			if steps[tracker][0] == steps[tracker-1][1] and not started:
				# print "------------------------------------"
				# print "Step: ",tracker
				# print "Start: ",steps[tracker][0]
				steps[tracker].append(steps[tracker-1][4])	# Push the ending point of the previous tracker into the step 
				started = True

			# If the step starting point is in the line
			elif steps[tracker][0] in line and not started:
				# print "------------------------------------"
				# print "Step: ",tracker
				# print "Start: ",steps[tracker][0]
				steps[tracker].append(line.split()[0])	# Push the starting time into the step
				started = True

			# If the step endig point is in the line
			elif steps[tracker][1] in line:
				# print "End: ",steps[tracker][1]
				steps[tracker].append(line.split()[0])	# Push the ending time into the step
				tracker += 1					# Start tracking next step
				started = False

			line_num += 1
				


		# Coordinates Parsing
		# coord_processor = Processor(lines)
		# coord_processor.parse()

		# Write duration to a csv
		step_csv = open("step_duration.csv","w")
		step_csv.write("Step,Duration,Start Time,End Time\n")

		for step in steps:
			start = datetime.strptime(step[-2].split(".")[0],"%H:%M:%S")
			end = datetime.strptime(step[-1].split(".")[0],"%H:%M:%S")
			diff = end - start
			step_csv.write("{0},{1},{2},{3}\n".format(step[-3].strip(),str(diff),step[-2],step[-1]))

		step_csv.close()


