#coding=UTF-8
import shutil
import os
import os.path

if __name__ == '__main__':
	src = u'幻灯片'
	des = 'pic'
	suffix = '.jpg'
	i = 1
	while i < 138:
	#	fsrc = open( src + str(i) + suffix, 'r')
	#	fdes = open( des + str(i) + suffix, 'w')
		shutil.copyfile(src + str(i) + suffix, des + str(i) + suffix )
	#	shutil.copyfile(fsrc, fdes )
		i += 1
