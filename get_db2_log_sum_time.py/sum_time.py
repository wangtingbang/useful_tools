import os
import sys
import time

def sum_time( infile, time_fmt, itm ):
	f = open( infile,'r')
	lines = f.readlines()
	bef = ''
	aft = ''
	count = 1
	all_tm = 0
	items = 6
	if -1 != itm:
		items = itm
#	print strftime(time.now() )
	for line in lines:
		line = line.rstrip()[0:19]
		if 1 == count:
			print '+++++++++++++++++++++++++++++++++++++++++++++'
			print 'At', line, 'started'
			bef = time.strptime( line, time_fmt )
			count += 1
		elif items == count:
			aft = time.strptime( line, time_fmt )
			count = 1
			print 'At', line, 'finished'
			sub_tm = (aft.tm_hour -bef.tm_hour ) * 60 * 60 + (aft.tm_min - bef.tm_min) *60 + ( aft.tm_sec - bef.tm_sec )
			print '---------------------------------------------'
			print 'This table in minute:', sub_tm / 60, 'and', sub_tm,'in second'
			print '=============================================\n'
			all_tm += sub_tm
		else:
			count += 1
	all_tm_by_sec = all_tm
	return all_tm_by_sec

if __name__ == '__main__':
	args = sys.argv
	time_fmt = '%Y-%m-%d %H:%M:%S'
	if len( args ) < 2:
		print 'error, input file path( exclude file name, just path ) to read please'
		print 'Usage:\n\tpython sum_time.py in_file time_formate out_file\n\tout_file can be null'
		exit()
	fpath = args[1]
	if len( args ) > 2:
		time_fmt = args[2]
	if len( args ) > 3:
		outfile = args[3]
		print outfile
	infile = fpath
	print time_fmt
	all_time = sum_time(infile, time_fmt, -1 )
	print 'All time:', all_time / 60 , 'min', all_time % 60, 's (', all_time, 'seconds in total )'
