__author__ = 'Administrator'

import re
contents = '<a href="/s/88c07fd3d8af09832336c03c06e7b49558c41f06/" title="">(C94) [ばーるみしゅ (ろんり)] 俺のオナホのエルドリッジ (アズールレーン)</a>(C94) [ばーるみしゅ (ろんり)] 俺のオナホのエルドリッジ (アズールレーン)</a><a href="/s/5ffe6d63c671a3f855816602db1ad4cf9db63d22/" title="">[Skytree][ONE PIECE 海贼王][892][X264][1080P][GB_BIG5_JP][MP4][CRRIP][简繁日中日双语内挂字幕]</a>'
print (contents)
patterns = re.compile('<a href=".*?" title="">(.*?)</a>')
result = re.findall(patterns,contents)
print(result)