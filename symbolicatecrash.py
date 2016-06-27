import sys
import getopt
from subprocess import check_output

def error(msg):
	if msg != None:
		print >>sys.stderr, msg
	print >>sys.stderr, "For help use -h"
	usage()

def usage():
	print >>sys.stderr, "##########"
	print >>sys.stderr, "# Usage: #"
	print >>sys.stderr, "##########"
	print >>sys.stderr, "symbolicatecrash.py -n <app_name> -c <crash_report> -a <architecture>"
	print >>sys.stderr, "Architectures: armv7, armv7s, arm64"

#####################################
#                                   #
#  Check that the dSYMs are correct #
#                                   #
#####################################

def check_uuid(app_name):
    try:        
        app_path = app_name + ".app/" + app_name
        dsym_path = app_name + ".app.dSYM"
        app_uuids = check_output(["dwarfdump", "--uuid", app_path])
        dsym_uuids = check_output(["dwarfdump", "--uuid", dsym_path])
        if uuids_from_output(app_uuids) == uuids_from_output(dsym_uuids):
            return 0
        else:
            print >>sys.stderr, "These are not the dSYMs for '" + app_name + "'"
            return 1
    except OSError as e:
        print >>sys.stderr, "Execution failed:", e
        return 1

def uuids_from_output(output):
    lines = output.split("\n")
    uuids = ""
    for line in lines:
        if line != '':
            components = line.split(" ")
            uuids += components[1] + " "
    return uuids.strip()

###############################################
#                                             #
#  Read the crash log and identify crash line #
#                                             #
###############################################

def find_crash_log(file_name):
	if file_name == None:
		return None

	f = open(file_name, 'r+')
	crashed_line_found = False
	for line in f:
		if crashed_line_found:
			f.close()
			return line 
		else:
			if "Crashed:" in line:
				crashed_line_found = True
	f.close()
	return None

def crash_addresses(line):
    components = line.split(" ")
    actual_components = []
    for c in components:
        if c != '':
            actual_components.append(c.strip())
    
    return (actual_components[3], actual_components[2]) if len(actual_components) > 2 else None

###########################
#                         #
#  Symbolicate crash line #
#                         #
###########################

def symbolicate_crash_line(app_name, crash_addresses, arch):
	app_path = app_name + ".app/" + app_name
	first = crash_addresses[0]
	second = crash_addresses[1]
	symbolicaded_line = check_output(["atos", "-o", app_path, "-arch", arch, "-l", first, second])
	if symbolicaded_line != None and symbolicaded_line != '':
		print >>sys.stdout, "Crash found at:"
		print >>sys.stdout, symbolicaded_line
	else:
		print >>sys.stderr, "Could not symbolicate"

#####################
#                   #
#  Parse parameters #
#                   #
#####################
def parse_parameters(opts, rem):
	app_name = None
	crash_report = None
	arch = None
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit(2)
		elif opt in ("-n", "--name"):
			app_name = arg
		elif opt in ("-c", "--crash"):
			if arg == None or arg == '':
				crash_report = rem[0] if len(rem) > 0 else None
			else:
				crash_report = arg
		elif opt in ("-a", "--arch"):
			if arg == None or arg == '':
				arch = rem[0] if len(rem) > 0 else None
			else:
				arch = arg

	return (app_name, crash_report, arch)

##################
#                #
#  Main function #
#                #
##################
def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        opts, rem = getopt.getopt(argv[1:], "hn:c:a", ["name", "crash", "arch"])
    except getopt.GetoptError, msg:
    	error(msg)
    	sys.exit(2)
    
    app_name, crash_report, arch = parse_parameters(opts, rem)
    if app_name == None or app_name == '' or crash_report == None or crash_report == '' or arch == None or arch == '':
    	print >>sys.stderr, "Error: Invalid parameters"
    	usage()
        sys.exit(2)
    else :
    	status = check_uuid(app_name)
        if  status == 0:
            crash_log_line = find_crash_log(crash_report)
            if crash_log_line != None:
                addresses = crash_addresses(crash_log_line)
                symbolicate_crash_line(app_name, addresses, arch)
            else:
        		print >>sys.stderr, "Error: Could not find crash line"
        		sys.exit(2)

if __name__ == "__main__":
    sys.exit(main())