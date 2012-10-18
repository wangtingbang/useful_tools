import re

def get_time( fpath, fnames, fout_tm ):
	ftime = fout_tm
	print fnames
	on = 0
	fout = open( ftime, 'w' )
	dat = ''
	for fname in fnames:
		f = open( fpath + '/' + fname, 'r')
		if f is None:
			continue
		print '\n+++++++++++++++++++++++++++++++++++++++++++++'
		print 'From', fname, 'read time record:'
		lines = f.read()
		patt = 'phase at time "(.*?)\n(.*?)".' #[0-9][0-9][0-9][0-9]"'
		prog = re.compile( patt, re.DOTALL )
		#print patt
		#print lines
		cont = prog.findall( lines )
		#print cont
		idx = 0
		for c in cont:
			print '\t',c[0] + c[1] 
			#fout = open( 'times/' + fname, 'a' )
			#fout.write( c[0] + c[1] + '\n' )
			dat += c[0] + c[1] + '\n'
			idx += 1
		#fout.write( "$$$\n" )
	fout.write(dat)
	rtn = [ftime, idx ]
	#return ftime
	return rtn

if __name__ == '__main__':
	import sys
	import os
	args = sys.argv
	if len( args ) < 2:
		print 'error, input file path( exclude file name, just path ) to read please'
		print 'Usage: python log_times.py in_file_dir time_formate out_file'
		print '\t\ttime_formate: "%Y-%m-%d %H:%M:%S" as default'
		print '\t\tout_file: can be null'
		exit()
	fpath = args[1]
	if len( args ) > 2:
		fout_time = args[2]
	else:
		fout_time = 'times/all_times.log'
	files = os.listdir( fpath )
	get_time( fpath, files, fout_time )
