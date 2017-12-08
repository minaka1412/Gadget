# coding: utf-8
# pylint: disable=C0103
"""
 * ファイル操作クラス
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import os
import shutil

class File(object):
    """
     * ファイル操作クラス
    """
    @staticmethod
    def Exists(path):
        """
         * ファイルが存在するか
         * I: str   path  処理対象のファイルパス
         * R: bool  True  存在
        """
        return os.path.isfile(path)

    @staticmethod
    def Rename(src, dst):
        """
         * ファイル名を変更する
         * I: str  src  変更前のファイルパス
         * I: str  dst  変更後のファイルパス
        """
        os.rename(src, dst)

    @staticmethod
    def Create(path, text):
        """
         * ファイルを新規作成する
         * I: str  path  作成するファイルのパス
         * I: str  msg   ファイルに書き込むテキスト
        """
        with open(path, 'w') as fobj:
            fobj.write(text)

    @staticmethod
    def Append(path, text):
        """
         * ファイルに追記する
         * I: str  path    作成するファイルのパス
         * I: str  msg     ファイルに書き込むテキスト
         * I: str  encode  ファイルを開く際のエンコード
        """
        with open(path, 'a') as fobj:
            fobj.write(text)

    @staticmethod
    def Load(path):
        """
         * ファイルを読み込む
         * I: str  path  読み込むファイルのパス
         * R: list       ファイルの内容
        """
        fileText = list()
        with open(path, 'r') as fobj:
            for row in fobj:
                fileText.append(row)
        return fileText

    @staticmethod
    def LoadBinary(path):
        """
         * ファイルをバイナリ形式で読み込む
         * I: str  path  読み込むファイルのパス
         * R: list       ファイルの内容
        """
        fileText = list()
        with open(path, 'rb') as fobj:
            for row in fobj:
                fileText.append(row)
        return fileText

    @staticmethod
    def Move(src, dst):
        """
         * ファイルを移動
         * I: str  src  移動元のファイルパス
         * I: str  dst  移動先のファイルパス
        """
        shutil.move(src=src, dst=dst)

    @staticmethod
    def Copy(src, dst):
        """
         * ファイルをコピー
         * I: str  src  移動元のファイルパス
         * I: str  dst  移動先のファイルパス
        """
        shutil.copy2(src, dst)

    @staticmethod
    def Delete(path):
        """
         * ファイルを削除
         * I: str  path  処理対象のファイルパス
        """
        os.remove(path)

File()
