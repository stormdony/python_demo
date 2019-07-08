##  Numpy矩阵计算器
![](https://img.shields.io/badge/build-Python3-green.svg) ![](https://img.shields.io/badge/author-donlex-yellowgreen.svg) ![](https://img.shields.io/badge/%E5%85%AC%E4%BC%97%E5%8F%B7-Python%E7%BB%BF%E6%B4%B2-blue.svg)

基于`pyqt`和`numpy`实现矩阵的计算功能。详细教程请参考[利用Numpy和PyQt5制作矩阵计算器](https://blog.csdn.net/stormdony/article/details/81359064)

## 编译环境

```bash
numpy        1.14.2
PyQt5        5.10.1
PyInstaller  3.3.1
PyQt5-sip    4.19.12
pyqt5-tools  5.9.0
```

## 文件说明
|  
|-**calc.ui**  使用`qtdesign`拖拽式生成的文件  
|-**calc.py**  使用`pyqt_tool`将`calc.ui`转换成的py文件  
|-**numpy_calc.py ** 总文件，将`calc.py`所有内容复制到这里，并添加其他代码  
 

## 效果
![](https://i.loli.net/2019/07/08/5d22ab252fece56357.png)