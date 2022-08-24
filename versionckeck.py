import sys, warnings
if sys.version_info[0] < 3:
    warning.warn("ff", RuntimeWarning)

else:
    print("This script is only for Python 3")