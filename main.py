import sys
from CoordinateParser import Processor
from StepParser import StepParser

# Open setupengine passed via commandline
logfile = open(sys.argv[1])

# Get all the lines
lines = logfile.readlines()

# Parse steps
stepParser = StepParser(lines)
stepParser.parse()

