import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
name = "delete" # exception dont
dont = "dont" # exception
exc = ".exe" # no exception

files = os.listdir(curr_dir)

store = []
for file in files:	
	if file.lower().endswith(exc) or (file.lower().find(dont) == -1 and file.lower().find(name) != -1):
		store.append(file)
for i in store:
	print(f"Deleting file {i}...")
	os.remove(i)
if len(store):
	print(f'Total file deleted {len(store)} with name including "{name}" or extention of "{exc}" with exception "{dont}" in names.')
else:
	print("No file to remove.")