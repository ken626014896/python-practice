#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ThreadLocal code

# encoding: UTF-8
import threading

local = threading.local()
local.tname = 'main'


def func():
    local.tname = 'notmain'
    print('%s tname = %s' %(threading.currentThread().name,local.tname))


t1 = threading.Thread(target=func)
t1.start()
t1.join()

print('%s tname = %s' %(threading.currentThread().name,local.tname))
