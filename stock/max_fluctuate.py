#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
import logging
import logging.config

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('stock')
