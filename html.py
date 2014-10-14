import random

_ = '''
<DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
</head>
<body>
</body>
</html>
'''

html_file = open(str(random.randint(0, 100)) + '.html', 'w')
html_file.write(_)
html_file.close()


