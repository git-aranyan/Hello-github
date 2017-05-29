
# -*- coding: utf-8 -*-

import sys

# Hello, python!と出力
print("Hello, Python!") # => Hello, Python!

# 変数
var = 10

# 変数の中身を出力
print(var) # => 10 3.14 Hello, Python!

num = 7 # int型(整数)
dec = 3.14 # float型(浮動小数点数)
string = "Hello, Python!" # str型(文字列)

#型名の出力
print(type(num)) # => <class 'int'>
print(type(dec)) # => <class 'float'>
print(type(string)) # => <class 'str'>

# 文字列操作
a = "Hello, "
b = "Python!"
# 連結
s = a + b
print(s)  # => Hello, Python!
# 繰り返し
print(b*2) # => Python!Python!
# 置換
print(s.replace("Python!","World!")) # => Hello, World!
# 分割
print(s.split(",")) # => ['Hello', ' Python!']
# n文字目取得
n = 1
print(s[n-1])
# スライス
