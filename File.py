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
    def Create(path, text, encode="utf-8_sig"):
        """
         * ファイルを新規作成する
         * I: str  path  作成するファイルのパス
         * I: str  msg   ファイルに書き込むテキスト
        """
        with open(path, 'w', encoding=encode, newline='') as file:
            file.write(text)

    @staticmethod
    def Append(path, text, encode="utf-8_sig"):
        """
         * ファイルに追記する
         * I: str  path    作成するファイルのパス
         * I: str  msg     ファイルに書き込むテキスト
         * I: str  encode  ファイルを開く際のエンコード
        """
        with open(path, 'a', encoding=encode, newline='') as file:
            file.write(text)

    @staticmethod
    def Load(path):
        """
         * ファイルを読み込む
         * I: str  path  読み込むファイルのパス
         * R: list       ファイルの内容
        """
        return File.__LoadEncodeText(path)

    @staticmethod
    def LoadList(path):
        """
         * ファイルを読み込む
         * I: str  path  読み込むファイルのパス
         * R: list       ファイルの内容
        """
        return File.__LoadEncodeText(path).split("\n")

    @staticmethod
    def __LoadEncodeText(path):
        """
        """
        encodeType = [
            "utf-8_sig",
            "utf-8",
            "shift-jis",
            "euc-jp",
            "utf-16",
            "utf-16-be",
            "utf-16-le",
            "utf-7",
            "euc-jisx0213",
            "euc-jis-2004",
            "iso-2022-jp",
            "iso-2022-jp-1",
            "iso-2022-jp-2",
            "iso-2022-jp-3",
            "iso-2022-jp-ext",
            "iso-2022-jp-2004",
        ]
        for encode in encodeType:
            try:
                with open(path, 'r', encoding=encode, newline='') as file:
                    return file.read()
            except UnicodeDecodeError:
                continue
        return None

    @staticmethod
    def LoadBinary(path):
        """
         * ファイルをバイナリ形式で読み込む
         * I: str  path  読み込むファイルのパス
         * R: list       ファイルの内容
        """
        fileText = list()
        with open(path, 'rb') as file:
            for row in file:
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
