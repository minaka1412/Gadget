# coding: utf-8
# pylint: disable=C0103
"""
 * システム関連クラス
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

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
        return platform.python_version_tuple()[0]

    @staticmethod
    def IsHostWindows():
        """
         * ホストOSがWindowsか
         * R:  bool  Windows時 True
        """
        return platform.system() == "Windows"

    @staticmethod
    def IsHostMac():
        """
         * ホストOSがMac OSか
         * R:  bool  Mac OS時 True
        """
        return platform.system() == "Darwin"

    @staticmethod
    def IsHostLinux():
        """
         * ホストOSがLinuxか
         * R:  bool  Linux時 True
        """
        return platform.system() == "Linux"

    @staticmethod
    def GetCpuCoreCount():
        """
         * 実行中のPCのCPUコア数を取得する
         * R:  int  CPUのコア数
        """
        return multiprocessing.cpu_count()

    @staticmethod
    def GetEnv(name):
        """
         * 環境変数を取得
         * I:  str  name  環境変数名
         * R:  str        環境変数の値
        """
        return str(os.environ[name])

    @staticmethod
    def GetEnvBool(name):
        """
         * 環境変数を取得
         * I:  str   name  環境変数名
         * R:  bool        環境変数の値
        """
        return System.GetEnv(name).lower() == "true"

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
        return subprocess.call(command, shell=True)

    @staticmethod
    def CallConsoleStr(command):
        """
         * システムコンソールでコマンドを実行
         * I:  str  command  実行するコマンド
         * R:  str           実行結果
        """
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

System()
