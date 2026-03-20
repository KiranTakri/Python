import zlib
str=b"This is advance python class"
com_data=zlib.compress(str)
decom_data=zlib.decompress(com_data)
print("String is compress ",com_data)
print("String is decompress ",decom_data)
