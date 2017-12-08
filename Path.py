# coding: utf-8
# pylint: disable=C0103
"""
 * ディレクトリパス操作クラス
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import os

class Path(object):
    """
     * ディレクトリパス操作クラス
    """
    # カレントディレクトリのスタックリスト
    __currentDirStack = list()

    @staticmethod
    def Combine(path1, *path2):
        """
         * 指定されたディレクトリパスを連結し、正規化する
         * I: str   path1  連結元のパス
         * I: list  path2  連結対象のパス
         * R: str          連結後のパス
        """
        retPath = path1
        for p in path2:
            retPath = os.path.join(retPath, p)
        return os.path.normpath(retPath)

    @staticmethod
    def GetDirectoryName(path):
        """
         * ディレクトリ名を取得
         * I: str  path  検索対象のパス
         * R; str        ディレクトリ名
        """
        return os.path.basename(os.path.dirname(path))

    @staticmethod
    def GetExtension(path):
        """
         * ディレクトリパスから拡張子を取得
         * I: str  path  検索対象のパス
         * R; str        拡張子名
        """
        return os.path.splitext(path)[1]

    @staticmethod
    def GetFileName(path):
        """
         * ファイル名を取得
         * I: str  path  検索対象のパス
         * R; str        ファイル名
        """
        return os.path.basename(path)

    @staticmethod
    def GetFileNameWithoutExtension(path):
        """
         * 拡張子を除いたファイル名を取得
         * I: str  path  検索対象のパス
         * R; str        ファイル名 (拡張子なし)
        """
        return os.path.basename(os.path.splitext(path)[0])

    @staticmethod
    def GetParentPath(path):
        """
         * 指定されたパスの一つ上のディレクトリパスへのパスを取得
         * I: str  path  検索対象のパス
         * R; str        ディレクトリ名
        """
        return os.path.normpath(os.path.dirname(path))

    @staticmethod
    def GetFullPath(path):
        """
         * 指定されたパスの絶対パスを取得
         * I: str  path  検索対象のパス
         * R; str        フルパス
        """
        return os.path.abspath(path)

    @staticmethod
    def ChangeExtension(path, extension):
        """
         * パス文字列の拡張子を変更
         * I: str  path       変更対象のパス
         * I: str  extension  変更後の拡張子
         * R: str             拡張子を変更したパス
         *                    元のパスに拡張子が存在しない場合は None
        """
        ext = Path.GetExtension(path)
        if ext is None or ext == "":
            return None
        return path.replace(ext, extension)

    @staticmethod
    def GetCurrentDir():
        """
         * カレントディレクトリを取得
         * R:  str  カレントディレクトリ
        """
        return os.getcwd()

    @staticmethod
    def SetCurrentDir(path):
        """
         * カレントディレクトリを設定
         * I:  str  path  新しいカレントディレクトリのパス
        """
        os.chdir(path)

    @staticmethod
    def PushCurrentDir(path):
        """
         * 現在のカレントディレクトリをスタックに保存し、カレントディレクトリを移動
         * I:  str  path  移動先のディレクトリパス
        """
        Path.__currentDirStack.append(Path.GetCurrentDir())
        Path.SetCurrentDir(path)

    @staticmethod
    def PopCurrentDir():
        """
         * スタックの最後に積まれたカレントディレクトリへ移動し、スタックから削除する
        """
        length = len(Path.__currentDirStack)
        if length > 0:
            Path.SetCurrentDir(Path.__currentDirStack[length - 1])
            del Path.__currentDirStack[length - 1]

Path()
