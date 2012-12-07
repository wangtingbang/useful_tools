import os
import re
import sys
import time

import get_time
import sum_time

all_time_log = 'times/all_times.log'

if __name__ == '__main__':
	args = sys.argv
	if len( args ) < 2:
		print 'error, input file path( exclude file name, just path ) to read please'
		print 'Usage: python log_times.py in_file_dir time_formate out_file'
		print '\t\ttime_formate: "%Y-%m-%d %H:%M:%S" as default'
		print '\t\tout_file: can be null'
		exit()
	fpath = args[1]
	time_fmt = '%Y-%m-%d %H:%M:%S'
	if len( args ) > 2:
		time_fmt = args[2]
	if len( args ) > 3:
		outfile = args[3]
		#print outfile
	files = os.listdir( fpath )
	print 'start get_time from log files.'
	fout_time = all_time_log
	rtn = get_time.get_time( fpath, files, fout_time )
	ftime = rtn[0]
	tm_items = rtn[1]
	print tm_items
	print 'start cumpute time sum'
	all_time = sum_time.sum_time( ftime, time_fmt, tm_items )
	print 'All time:', all_time / 60 , 'min', all_time % 60, 's (', all_time, 'seconds in total )'
	exit()
