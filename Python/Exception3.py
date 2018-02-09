try:
    1/0
    pass

except ValueError:
   pass

except (TypeError, ZeroDivisionError):
    print('exception caught')
    pass

except:
    pass
