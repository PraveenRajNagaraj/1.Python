try:
    a=int(input())
    b=int(input())
except ValueError as e:
    print("ValueError",e)
except TypeError as e:
    print("Type Error",e)
except Exception:
    print("something wrong")
finally:
    print("Done")
