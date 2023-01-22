#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_tm1 import SourceTM1

if __name__ == "__main__":
    source = SourceTM1()
    launch(source, sys.argv[1:])
