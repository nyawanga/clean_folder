import os
import argparse
import shutil

documents = ['.pdf', '.doc', '.docx', '.txt','.csv', '.xlsx', '.pptx']
videos = ['.mp4', '.mpeg', '.mkv']
programs = ['.deb', '.exe', '.msi']
compressed = ['.zip','.rar','.gz','.tar','.tar.gz']
scripts = ['.py', '.sql']
audios = ['.mp3']
images = ['.jpeg', '.png', '.jpg']

def get_dir_list(target_path):
	os.chdir(target_path)
	content = os.listdir()

	for item in content:
		if os.path.isfile(item):
			yield item, 'file'
		elif os.path.isdir( item):
			yield item, 'dir'

def create_folder(target_path, new_folder):
	os.chdir(target_path)
	folder_path = os.path.join(target_path, new_folder)
	try:
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)
	except OSError as e:
		print("OSError incurred \n{}".format(e) )

def extract_extension(file, type):
    if type == 'file':
        ext = os.path.splitext(file)[-1]
        return ext
    else:
        return None

def move_files(target_path):
	os.chdir(target_path)
	item = get_dir_list(target_path)
	list_empty = False
	while not list_empty:
		try:
			file, file_type = next(item)
			file_ext = extract_extension( file, file_type )
			#current_path = os.path.join(args.directory, file)
			current_path = os.path.abspath(file)
			#print(file)
			if file_ext in documents:
				create_folder(target_path, 'documents')
				change = 'documents/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to documents'.format(file) )
			elif file_ext in videos:
				create_folder(target_path, 'videos')
				change = 'videos/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('videos :', file )
			elif file_ext in audios:
				create_folder(target_path, 'audios')
				change = 'audios/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to audios'.format(file) )
			elif file_ext in images:
				create_folder(target_path, 'images')
				change = 'images/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to images'.format(file) )
			elif file_ext in scripts:
				create_folder(target_path, 'scripts')
				change = 'scripts/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to scripts'.format(file) )
			elif file_ext in programs:
				create_folder(target_path, 'programs')
				change = 'programs/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to programs'.format(file) )
			elif file_ext in compressed:
				create_folder(target_path, 'compressed')
				change = 'compressed/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to compressed'.format( file) )
			elif not file_ext is None:
				create_folder(target_path, 'unknown')
				change = 'unknown/' + file
				new_path = os.path.join(target_path, change)
				shutil.move(current_path, new_path)                   #move the file
				print('moved {} to unknown'.format(file) )
			else:
			#   print('Is a directory:', file)
			    pass
		except StopIteration as e:
			#print("End of list")
			list_empty = True
		except Exception as e:
			print("Unexpected error \n{}".format(e) )

def main():
	global documents, audio, videos, scripts, compressed, programs
	parser = argparse.ArgumentParser(description = 'Get cleaning parameters')
	parser.add_argument('-D', '--directory', required  = True, metavar='',
                      type = str,help ="absolute path to directory to be cleaned ending with '/' ")

	args = parser.parse_args()
	os.chdir(args.directory)
	move_files(args.directory)

	print([i for i in os.listdir(args.directory)] )

if __name__ == "__main__":
	main()
