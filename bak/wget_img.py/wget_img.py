import sys
import os
if __name__ == '__main__':
	argv = sys.argv
	print argv
	os.system( 'wget ' + argv[1]);
