#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import config

module_version = config.VERSION
module_name = "{0}.run".format(module_version)

module = importlib.import_module(module_name)

if __name__ == "__main__":
    module.run(config.IP, config.PORT, config.THREADED, config.DEBUG)