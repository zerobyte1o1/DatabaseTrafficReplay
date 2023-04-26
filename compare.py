import sqlparse

# 读取两个备份文件
with open('test3_scm.sql', 'r') as f1:
    data1 = f1.read()

with open('test3_scm_1.sql', 'r') as f2:
    data2 = f2.read()

# 解析SQL语句
parsed1 = sqlparse.parse(data1)
parsed2 = sqlparse.parse(data2)

# 比较差异
diff = sqlparse.parse(sqlparse.format(parsed2[0], reindent=True, keyword_case='upper'))
for stmt in sqlparse.parse(sqlparse.format(parsed1[0], reindent=True, keyword_case='upper')):
    if stmt not in diff:
        print(sqlparse.format(stmt, reindent=True))