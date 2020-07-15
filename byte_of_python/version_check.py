#!/usr/bin/env python3
import sys
import warnings

if sys.version_info[0] < 3:
    warnings.warn(
        "Execution of the program needs minimum Python 3.0",
        RuntimeWarning
    )
else:
    print('Normal work.')