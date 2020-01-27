# robosyskadai2

# システムの概要  
入力された数字の足し算を行うパッケージ．  
入力された数字をrostopicとしてパブリッシュし、それをサブスクライブして足し合わせる．  
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
`$ rosrun robosyskadai2 pub_num.py`  
端末３  
`$ rosrun robosyskadai2 sub_num.py`

## YouTube
https://youtu.be/jxKyGvWS4fg

## 一緒にやった人
木村　慧士　https://github.com/kimurasatoshi
小島　健　　https://github.com/Takeshi-Kojima
吉村　一希　https://github.com/kazuki0702

## LICENSE  
This repository is licensed under the BSD-3-Clause license, see LICENSE.
