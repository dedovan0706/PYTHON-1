new file function_file.py file hello.py

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

    import function_file
    print(function_file.f(1)) # Целое
    print(function_file.f(2.3)) # 23
    print(function_file.f(28)) # None