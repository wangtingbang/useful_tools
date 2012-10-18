+log_times.py:
	-input:
		i>. db2 load message files dir, not filename;
		ii>.date(time) formate if necessary;
		iii>.output file, can be null.
	-processing:
		
	-usage: python log_times.py ./log "%Y-%m-%d %H:%M:%S"

+get_time.py:

	-Usage: python log_times.py in_file_dir time_formate out_file
			time_formate: "%Y-%m-%d %H:%M:%S" as default
			out_file: can be null

+sum_time.py:
	-Usage: python sum_time.py in_file time_formate out_file
		time_formate: "%Y-%m-%d %H:%M:%S" as default
		out_file: can be null

+example:
	-cmd:
		>> python log_times.py ./log "%Y-%m-%d %H:%M:%S"
		>> python get_time.py ./log
		>> python sum_time.py times/all_times.log
	-files( ls -R ):
		.:
			ReadMe.txt sum_time.py get_time.py log_times.py times log
		./log:
			ECIFMODEL.ADDRESS.log  ECIFMODEL.CONTACT.log  ECIFMODEL.PERSON.log
		./times:
			all_times.log
