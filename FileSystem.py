# coding: utf-8
# pylint: disable=C0103
"""
 * ファイル・ディレクトリ操作クラス群
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import glob
import os

class FileSystem(object):
    """
     * ファイル・ディレクトリ操作クラス
    """
    @staticmethod
    def GetDirectoryList(path, recursive=False):
        """
         * 指定されたディレクトリ内に存在するファイル・フォルダのリストを取得
         * I;  str   path       検索対象のディレクトリパス
         * I:  bool  recursive  再帰的にチェックするか
         * R:  list             ファイル・フォルダのリスト
        """
        from Gadget.Path import Path
        retList = list()
        if recursive:
            for root, dirs, files in os.walk(path):
                for d in dirs:
                    retList.append(Path.Combine(root, d))
                for f in files:
                    retList.append(Path.Combine(root, f))
        else:
            for name in os.listdir(path):
                retList.append(Path.Combine(path, name))
        return retList

    @staticmethod
    def GetFileList(path, extension="*.*", recursive=False):
        """
         * 指定されたディレクトリ内に存在するファイルのリストを取得
         * I;  str   path       検索対象のディレクトリパス
         * I:  str   extension  検索するファイルの拡張子
         * I:  bool  recursive  再帰的にチェックするか
         * R:  list  ファイルのリスト
        """
        from Gadget.Path import Path
        if recursive:
            retList = list(glob.glob(Path.Combine(path, extension)))
            dirList = FileSystem.GetFolderList(path, recursive=recursive)
            for dirPath in dirList:
                retList.extend(list(glob.glob(Path.Combine(dirPath, extension))))
            return retList
        return list(glob.glob(Path.Combine(path, extension)))

    @staticmethod
    def GetFolderList(path, recursive=False):
        """
         * 指定されたディレクトリ内に存在するフォルダのリストを取得
         * I;  str   path       検索対象のディレクトリパス
         * I:  bool  recursive  再帰的にチェックするか
         * R:  list             フォルダのリスト
        """
        from Gadget.Directory import Directory
        retList = list()
        dirList = FileSystem.GetDirectoryList(path, recursive=recursive)
        for dirPath in dirList:
            if Directory.Exists(dirPath):
                retList.append(dirPath)
        return retList

    @staticmethod
    def CreateSymbolicLink(srcPath, dstPath):
        """
         * シンボリックリンクを作成する
         * I:  str   srcPath  作成元のディレクトリパス
         * I:  str   dstPath  作成先のディレクトリパス
        """
        try:
            os.symlink(srcPath, dstPath)
        except OSError as e:
            print("OSError: " + e)

FileSystem()
