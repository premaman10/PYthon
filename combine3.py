Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> . for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i != j and j != k and i != k:
                print(i, j, k)
