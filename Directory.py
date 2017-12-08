# coding: utf-8
# pylint: disable=C0103
"""
 * ディレクトリ操作クラス
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import os
import shutil

class Directory(object):
    """
     * ディレクトリ操作をまとめたクラス
    """
    @staticmethod
    def Exists(path):
        """
         * ディレクトリが存在するか
         * I: str   path  処理対象のディレクトリパス
         * R: bool  True  存在
        """
        return os.path.isdir(path)

    @staticmethod
    def Rename(src, dst):
        """
         * ディレクトリ名を変更する
         * I: str  src  変更前のディレクトリパス
         * I: str  dst  変更後のディレクトリパス
        """
        os.rename(src, dst)

    @staticmethod
    def Create(path):
        """
         * ディレクトリを作成
         * I: str   path  処理対象のディレクトリパス
        """
        os.makedirs(path)

    @staticmethod
    def Move(src, dst):
        """
         * ディレクトリを移動
         * I: str  src  移動元のディレクトリパス
         * I: str  dst  移動先のディレクトリパス
        """
        shutil.move(src=src, dst=dst)

    @staticmethod
    def Copy(src, dst):
        """
         * ディレクトリをコピー
         * I: str  src  コピー元のディレクトリパス
         * I: str  dst  コピー先のディレクトリパス
        """
        shutil.copytree(src, dst)

    @staticmethod
    def Delete(path):
        """
         * ディレクトリを削除
         * I: str  path  処理対象のディレクトリパス
        """
        shutil.rmtree(path)

Directory()
