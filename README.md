# robosyskadai2

# システムの概要  
入力された数字をポンドとして認識しキログラムに変換する  
ポンドで入力された数字をパブリッシュして、それをサブスクライブしてキログラムに変換するパッケージ  
## 手法  
### インストール手順
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/KosekiTakashi/robosyskadai2.git
$ cd ../
$ catkin_make
```    
## 実行  
端末１  
`$ roscore`  
端末２  
`$ rosrun robosyskadai2 pub_pond.py`  
端末３  
`$ rosrun robosyskadai2 sub_pond.py`
## YouTube
https://youtu.be/jxKyGvWS4fg

## LICENSE  
This repository is licensed under the BSD-3-Clause license, see LICENSE.
