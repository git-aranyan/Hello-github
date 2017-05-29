
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
s = "1234567"
print(s[0]) # => 1
print(s[3:7]) # => 4567
print(s[::2]) # => 1357
print(s[::-1]) # => 7654321


# if文
num = 64
if num < 0:
    print("negative")
elif num > 0:
    print("positive")
else:
    print("zero")    # => positive

# while文
n = 0               # =>
while n < 10:       #   1
    print(n)        #   2
    n += 1          #   3
else:               #   ...9
    print("END")    #   END

# for文いろいろ
for i in range(10):
    print(i)


for i in (1,3,5,7,9):
    print(i)

#リストを使ったfor文
words = ['C','Go','Java','Python']
for i in words:
    print(i)


#リスト
li = ['Bear','Bird','Snake','Rat']
print(type(li)) # => <class 'list'>

#タプル
tp = ('Fortran','Lisp','Prolog','Basic')
print(type(tp)) # => <class 'tuple'>

#辞書
dr = {1:'cat',2:'dog',3:'rabbit'}
print(type(dr)) # => <class 'dict'>

# 関数
def func(var, *args, var2 = "default", **d):
    print(var) #=> A
    print(var2)  #=> default
    print(args) #=> ('B','C', 'D')
    print(d) #=> {'k1': 'Python', 'k2': 'Ruby'}

func('A', 'B', 'C', 'D', k1='Python', k2='Ruby')

# クラス，（）内のクラスを継承
class ClassName(object):
    # クラス変数
    c_var = "クラス変数"
    # コンストラクタ，argはクラスを呼ぶときの引数
    def __init__(self, arg):
        # 親クラスのコンストラクタの呼び出し
        super(ClassName,self).__init__()
        # インスタンス変数
        self.i_var = arg
        print("インスタンスが生成された")
    # メソッド
    def func(self):
        print("メソッドが呼び出された")
# インスタンスの生成
hoge = ClassName("インスタンス変数") # => インスタンスが生成された

# インスタンスのメソッドの呼び出し
hoge.func() # => メソッドが呼び出された
# インスタンス変数の呼び出し
print(hoge.i_var) # => インスタンス変数
# クラス変数の呼び出し
print(ClassName.c_var) # => クラス変数
