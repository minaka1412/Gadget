# coding: utf-8
# pylint: disable=C0103
"""
 * システム関連クラス
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import ctypes
import multiprocessing
import os
import platform
import subprocess
import sys

class System(object):
    """
     * システム関連クラス
    """
    @staticmethod
    def GetUsePythonVersion():
        """
         * 使用中のPythonのバージョンを取得する
         * R: int  2 or 3
        """
        return int(platform.python_version_tuple()[0])

    @staticmethod
    def IsHostWindows():
        """
         * ホストOSがWindowsか
         * R:  bool  Windows時 True
        """
        return bool(platform.system() == "Windows")

    @staticmethod
    def IsHostMac():
        """
         * ホストOSがMac OSか
         * R:  bool  Mac OS時 True
        """
        return bool(platform.system() == "Darwin")

    @staticmethod
    def IsHostLinux():
        """
         * ホストOSがLinuxか
         * R:  bool  Linux時 True
        """
        return bool(platform.system() == "Linux")

    @staticmethod
    def IsAdmin():
        """
         * 管理者権限で実行しているか
         * Windows環境下のみ動作
         * R:  bool  管理者権限で実行時 True
        """
        try:
            if System.IsHostWindows():
                return ctypes.windll.shell32.IsUserAnAdmin()
            else:
                return False
        except:
            return False

    @staticmethod
    def GetAndRunAdminPermission(func=None):
        """
         * 管理者権限で再実行
         * Windows環境下でのみ動作
         * I:  def   func  実行する関数ポインタ
         * R:  bool  管理者権限で実行時 True
        """
        if System.IsAdmin():
            if func is not None:
                func()
            return True
        else:
            System.GetAdminPermission(sys.argv[0])
            return False

    @staticmethod
    def GetAdminPermission(callFile):
        """
         * スクリプトを管理者権限で再実行
         * Windows環境下でのみ動作
         * I:  str   callFile  呼び出し元のファイル名
         * FROM: https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
        """
        if System.IsHostWindows():
            version = System.GetUsePythonVersion()
            if version == 3:
                ctypes.windll.shell32.ShellExecuteW(
                    None, "runas", sys.executable, callFile, None, 1)
            elif version == 2:
                ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(
                    sys.executable), unicode(callFile), None, 1)

    @staticmethod
    def GetCpuCoreCount():
        """
         * 実行中のPCのCPUコア数を取得する
         * R:  int  CPUのコア数
        """
        return int(multiprocessing.cpu_count())

    @staticmethod
    def GetEnv(name):
        """
         * 環境変数を取得
         * I:  str  name  環境変数名
         * R:  str        環境変数の値
        """
        return System.ToString(os.environ[name])

    @staticmethod
    def GetEnvBool(name):
        """
         * 環境変数を取得
         * I:  str   name  環境変数名
         * R:  bool        環境変数の値
        """
        return bool(System.GetEnv(name).lower() == "true")

    @staticmethod
    def GetEnvInt(name):
        """
         * 環境変数を取得
         * I:  str  name  環境変数名
         * R:  int        環境変数の値
        """
        return int(System.GetEnv(name))

    @staticmethod
    def SetEnv(name, val):
        """
         * 環境変数を設定
         * I:  str  name  環境変数名
         * I:  str  val   環境変数の値
        """
        os.environ[name] = val

    @staticmethod
    def GetArgv():
        """
         * コマンドライン引数を取得
         * R:  str[]  コマンドライン引数配列
        """
        return sys.argv

    @staticmethod
    def CallConsoleInt(command):
        """
         * システムコンソールでコマンドを実行
         * I:  str  command  実行するコマンド
         * R:  int           実行結果
        """
        return int(subprocess.call(command, shell=True))

    @staticmethod
    def CallConsoleStr(command):
        """
         * システムコンソールでコマンドを実行
         * I:  str  command  実行するコマンド
         * R:  str           実行結果
        """
        ret = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        return System.ToString(ret)

    @staticmethod
    def ToString(data, encodeType="utf-8_sig"):
        """
         * 引数の文字列かバイト列を文字列に変換する
         * I: str or byte  data        変換対象のデータ
         * I: str          encodeType  変換後の文字列のエンコード形式
         * R: str                      変換後のデータ
        """
        pythonVersion = System.GetUsePythonVersion()
        if pythonVersion == 3:
            if isinstance(data, str):
                return data
            return str(data.decode(encodeType))
        elif pythonVersion == 2:
            if isinstance(data, unicode):
                convStr = data.encode(encodeType)
            else:
                try:
                    uniStr = data.decode(encodeType)
                except UnicodeDecodeError:
                    try:
                        uniStr = data.decode('utf-8')
                    except UnicodeDecodeError:
                        uniStr = data.decode('shift-jis')
                convStr = uniStr.encode(encodeType)
            return convStr
        return data

System()
