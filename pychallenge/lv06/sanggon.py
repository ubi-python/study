from zipfile import *

start_number = '90052'
nothing_list = list()
try:
    with ZipFile('channel.zip', 'r') as channelZip:
        file_name_list = channelZip.namelist()
        for filename in file_name_list:
            with channelZip.open(filename) as nothing_file:
                lines = nothing_file.readlines()
                for l in lines:
                    words = str(l.decode('utf-8')).split(' ')
                    nothing_list.append(words[len(words) - 1])
            print('=================================')
except BadZipfile:
    print('Bad Zip file')

print(file_name_list)
print(nothing_list)
