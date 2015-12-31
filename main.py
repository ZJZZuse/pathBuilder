# coding=utf-8
__author__ = 'wb-zhangjinzhong'

import os
import os.path

import myCommonToolsZ
import myDataTools

tz = myCommonToolsZ

rootdir = 'D:/abc/t/img'  # 指明被遍历的文件夹

if __name__ == '__main__':
    # list = acqFileList(rootdir, [])
    # for e in list:
    #     print e
    #
    # print

    # for f in acqFirstFolders(rootdir):
    #     print f

    # for e in acqFiles(rootdir,parentFolderNamePreDispose=lambda s: s.replace(rootdir + '\\','')):
    #     print e['name'], e['path'], e['parentFolderName']
    #
    # for e in acqFirstFolders(rootdir):
    #     print e

    tableCfg = {

        'name':'',
        'path':'',
        'parentFolderName':''

    }

    myDataTools.DataWrapper.initDb('imgTest.db')

    wrapper = myDataTools.DataWrapper('imgs', myDataTools.DataWrapper.wrappeByCommonFieldCfg(tableCfg))

    for ele in tz.acqFilesInRelPath(rootdir):
        wrapper.add(ele)



# windows下为：d:\data\query_text\EL_00154
