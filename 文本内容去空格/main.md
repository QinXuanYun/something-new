### 在主项目中某些知识点直接复制电子版书本的，但某些原因造成复制黏贴后有空格，影响编辑，而用的瑞士军刀这个功能个人觉得有点麻烦，因此用py写了个去空格的小东西

---
import pyperclip as pc  # 导入"pyperclip"模块进行剪切板复制黏贴操作，将其在本项目中命名为pc，方便后续使用
     
a = input("")  # 将输入内容赋值给a     
b = a.replace(" ", "")  # 将a中空格替换为"无内容"，并赋值给b     
pc.copy(b)  # 通过上述模块实现将b复制到剪切板     
c = pc.paste()  # 通过黏贴剪切板操作将内容赋值给c     
print(c)  # 输出c（实际c就是b）     
print(type(c))     
temps = input("\n") #这个功能是直接执行py文件（默认cmd结合python.exe）时保留窗口）虽然需要的内容已经复制到剪切板了，没啥用(我是这么理解的，实际作用暂未探究)

---

Todo:探究"temps = input("\n")"的作用及……

---

## 精简版

---

import pyperclip as pc

a = input("")     
b = a.replace(" ", "")     
pc.copy(b)
