import subprocess
import configparser
import os

# 获取数据库基本配置
config = configparser.ConfigParser()
current_dir = os.path.abspath(os.getcwd())
print(current_dir)
config.read(current_dir+'/config/config.ini')
username = config.get('database', 'username')
password = config.get('database', 'password')
host = config.get('database', 'host')
port = config.get('database', 'port')
database_name = config.get('database', 'database_name')
# 备份数据库
result = subprocess.run(['pg_dump', '-U', username, '-h', host,'-p',port, database_name], stdout=subprocess.PIPE)
backup_data = result.stdout.decode('utf-8')

# 设置文件名后缀
filename_suffix = '.sql'

# 初始化文件名计数器
filename_counter = 1

# 检查文件是否存在，如果存在，则增加计数器
while os.path.exists(os.path.join(current_dir, f"{database_name}_{filename_counter}{filename_suffix}")):
    filename_counter += 1

# 生成新的文件名
new_filename = f"{database_name}_{filename_counter}{filename_suffix}"

# 将备份数据写入文件
with open(new_filename, 'w') as f:
    f.write(backup_data)

