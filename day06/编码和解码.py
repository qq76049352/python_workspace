# s = 'alex'
# print(s.encode('utf-8'))  #b'alex'

s = "饿了"
s1 = s.encode("utf-8")  #b'\xe9\xa5\xbf\xe4\xba\x86\xe5\x90\x97'
# print(s.encode("gbk"))    #b'\xb6\xf6\xc1\xcb\xc2\xf0'

print(s1.decode('utf-8'))

