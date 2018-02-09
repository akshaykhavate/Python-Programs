import sys
try:
    1/0
except Exception:
    exec_tuple=sys.exec_info()
