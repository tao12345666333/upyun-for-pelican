#!/usr/bin/python
#-*- encoding:utf-8 -*-

import upyun
import os
import sys
from pelicanconf import *

reload(sys)
sys.setdefaultencoding('utf-8')

def formatPath(path):
	path = path.replace(os.sep, '/')
	return path

def uptoBucket(local_up_dir, bucket):
	"""Upload files to upyun bucket.

	Args:
	    local_up_dir: The local directory which will be upload.
	    bucket: The bucket name and some infos.
	"""
	def toBucketPath(local_up_dir, local_path):
		path = local_path.replace(local_up_dir, '', 1)
		if len(path) == 0:
			path = formatPath('/')
		elif path[0] != '/' :
			path = formatPath('/' + path)
		return path

	dirs_list = []
	files_list = []

	for root_path, _, files in os.walk(local_up_dir):
		dirs_list.append(formatPath(root_path))
		if len(files) > 0:
			for filename in files:
				files_list.append(formatPath(root_path + '/' + filename))
		dirs_list.sort (key=lambda x:len(x))
	dirs_list.remove(formatPath(local_up_dir))

	print 'start make directory in bucket...'

	for d in dirs_list:
		print d, '-->', toBucketPath(local_up_dir, d).encode('utf-8')

	print 'start upload files to bucket...'

	for filename in files_list:
		print filename, '-->', toBucketPath(local_up_dir.encode('utf-8'), filename)
		with open(filename, 'rb') as f:
			try:
				bucket.put(toBucketPath(local_up_dir, filename).encode('utf-8'), f, checksum=True, headers=None)
			except Exception, e:
				print e

def main(BUCKETNAME, USERNAME, PASSWORD, local_dir):

	print 'Welcom to upyun for pelican....'	
	decide =  raw_input('Do you want to upload your output directory ( Y / N ?)')

	if decide=='Y' or decide=='y':
		upyun_bucket = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30, endpoint=upyun.ED_AUTO)
		uptoBucket( local_dir, upyun_bucket)
		print('==================================================')
		print 'Congratulations on your file upload is complete'
		print('==================================================')
	elif decide=='N' or decide=='n':
		print 'You choose NO the program will exit...'
	else:
		print 'Input errors, please re-enter.'

if __name__ == '__main__':
	local_dir = './output'
	main(BUCKETNAME, USERNAME, PASSWORD, local_dir)
