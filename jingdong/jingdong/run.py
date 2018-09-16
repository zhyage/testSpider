# -*- coding: utf-8 -*-

from scrapy import cmdline
name = 'jingdong'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())

#用于在IDE里进行Debug
