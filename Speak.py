#!/usr/bin/env python3
"""

"""

# Allow the use of the AWS SDK in Python
# https://pypi.org/project/boto3/
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

from contextlib import closing

import os
import sys

import subprocess

from tempfile import gettempdir


