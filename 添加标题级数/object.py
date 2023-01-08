import pyperclip as pc

a = ["", "#", "##", "###", "####", "#####", "######"]
b = int(input("请输入级数:"))
c = input("请输入内容:")
if b == 0:
    pc.copy(a[b] + c)
else:
    pc.copy(a[b] + " " + c)
