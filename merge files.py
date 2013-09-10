import os

# 文件夹操作 folder
path_name = input('请输入文件夹路径 Pleaase input the folder：\n')
if os.path.isdir(path_name):
    os.chdir(path_name)
    file_list = os.listdir(path_name)
    print(file_list)
else:
    print('目录不存在 No such folder')
    sys.exit()

# 建立文件, use markdown format because it's easy for web use
file_name = input('请输入要生成的文件名 Please name the file to be created:\n')
file_dist = open(file_name+'.md', 'wb')
file_dist.truncate()
for files in file_list:
    file_source = open(files, 'rb')
    file_content = file_source.read()
    print(file_content)
# use file name as paragraphy header    
    file_dist.write(str('# '+files + ' #' +'\n').encode('utf-8'))
    file_dist.write(file_content)
    file_source.close()
file_dist.close()
print(file_dist)
