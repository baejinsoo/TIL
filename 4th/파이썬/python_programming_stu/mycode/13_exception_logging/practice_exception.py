# try ~ except ~ else

# try ~ except ~ finally

for i in range(10):
    try:
        result = 10 / i
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        print('종료되었음')


