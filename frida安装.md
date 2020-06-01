# Frida安装

## 1. 部署Python运行环境 （略）


## 2. 安装Frida

#### 1. pip install frida
#### 2. pip install frida-tools
#### 3. 下载frida-server，在github
 地址：https://github.com/frida/frida/releases

譬如现在frida-server最新版本是12.8.10 . 
CPU型号查询指令`adb shell getprop ro.product.cpu.abi`
那么就下载**frida-server-12.8.10-android-（CPU型号）.xz**

#### 4.传文件到android设备上

	adb push frida-server /data/local/tmp/
	adb shell
	su
	cd data/local/tmp
	chmod 777 frida-server

#### 5.测试

	./frida-server

打开一个新的terminal

	frida-ps -U

这行命令是列出手机上所有的进程信息，如果出现进程信息则说明环境搭配成功

#### 6.端口转发

	adb forward tcp:27042 tcp:27042
	adb forward tcp:27043 tcp:27043

	frida-ps -R

可以看到android机器的进程列表了，至此，运行环境就搭建好了。

## 3.frida初次体验

	import frida
	
	remote_dev = frida.get_remote_device()
	print(remote_dev)
	front_app = remote_dev.get_frontmost_application()
	print(front_app)
	
	process = remote_dev.enumerate_processes()
	for i in process:
	    print(i)

返回结果:
	
	Device(id="tcp", name="Local TCP", type='remote')
	Application(identifier="com.microvirt.launcher", name="逍遥桌面", pid=756)
	Process(pid=1, name="init")
	Process(pid=44, name="ueventd")
	Process(pid=54, name="systemd")
	Process(pid=55, name="run")
	Process(pid=56, name="logd")
	.......
	Process(pid=8530, name="fdax86")
	Process(pid=8532, name="logcat")
	
	Process finished with exit code 0

## 4.工具介绍

Frida提供了四个工具，frida-trace，frida-ps，frida，frida-discover，这些工具都位于python的Scripts路径下，不多说

## 5.frida接口

#### 1. python 接口

python接口提供的功能很少，而且基本都是用来获取进程、模块、函数的信息的。

python接口的实现都在frida-python里面了。

Python提供了一些全局接口，在文件frida-python \scr\frida\_init_.py里面
其中Get_usb_device可以获取当前连接到usb的设备，如果使用手机，一般使用这个函数获取手机设备。

而其他的接口都在frida-python /src/frida/core.py里面，比如进程、模块、函数相关的操作..

**
这里需要注意的是，在使用frida的时候，首先第一步要做的是获取设备，我这里使用get_usb_device来获取手机设备，然后第二步要做的是指定要附加的进程。**

#### 2. js接口
js接口就相当丰富了，接口功能包括但不限于进程操作、模块操作、内存操作、函数操作、线程操作、网络通信、数据流操作、文件操作、数据库操作、寄存器操作，并且官网有着详细的说明文档https://www.frida.re/docs/javascript-api/，对于每个接口的功能和参数给出了详细的解释，并且一部分接口还给出了例子。

下面来看一个遍历进程模块的简单示例。


