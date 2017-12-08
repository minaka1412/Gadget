# coding: utf-8
# pylint: disable=C0103
"""
 * ログ出力管理クラス
 * Development by minaka1412
"""
from __future__ import division, print_function, absolute_import, unicode_literals

import logging

class Logger(object):
    """
     * ログ出力管理クラス
    """
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    DEFAULT_FORMAT = "%(asctime)s %(levelname)-8s %(message)s"

    m_logger = None
    m_handler_dict = dict()

    def __init__(self):
        """
         * 初期化
        """
        Logger.m_logger = logging.getLogger()
        logging.basicConfig(level=self.DEBUG, format=self.DEFAULT_FORMAT, datefmt="%H:%M:%S")

    @staticmethod
    def SetLevel(level):
        """
         * 出力するログのレベルを指定
         * I:  Logger.*  level  出力するログのレベル
        """
        Logger.m_logger.setLevel(level)
        for handler in Logger.m_handler_dict:
            handler.setLevel(level)

    @staticmethod
    def AddOutputFile(path):
        """
         * 追加出力先のファイルを追加する
         * I:  str  path  追加出力先のファイルパス
        """
        # 出力先のフォルダを作成しておく
        from Directory import Directory
        from Path import Path
        parentPath = Path.GetParentPath(path)
        if not Directory.Exists(parentPath):
            Directory.Create(parentPath)

        # ハンドラ登録
        file_handler = logging.FileHandler(path, 'w')
        file_handler.formatter = logging.Formatter(fmt=Logger.DEFAULT_FORMAT, datefmt="%H:%M:%S")
        file_handler.level = Logger.DEBUG
        Logger.m_handler_dict[path] = file_handler
        Logger.m_logger.addHandler(file_handler)

    @staticmethod
    def CloseOutputFile(path):
        """
         * 追加出力先のファイルを閉じる
         * I:  str  path  閉じる追加出力先のファイルパス
        """
        file_handler = Logger.m_handler_dict[path]
        file_handler.close()
        Logger.m_logger.removeHandler(file_handler)
        del Logger.m_handler_dict[path]

    @staticmethod
    def Log(msg):
        """
         * レベル DEBUG のログを出力
         * I:  str  msg  出力するメッセージ
        """
        Logger.Debug(msg)

    @staticmethod
    def Debug(msg):
        """
         * レベル DEBUG のログを出力
         * I:  str  msg  出力するメッセージ
        """
        Logger.m_logger.debug(msg)

    @staticmethod
    def Info(msg):
        """
         * レベル INFO のログを出力
         * I:  str  msg  出力するメッセージ
        """
        Logger.m_logger.info(msg)

    @staticmethod
    def Warning(msg):
        """
         * レベル WARNING のログを出力
         * I:  str  msg  出力するメッセージ
        """
        Logger.m_logger.warning(msg)

    @staticmethod
    def Error(msg):
        """
         * レベル ERROR のログを出力
         * I:  str  msg  出力するメッセージ
        """
        Logger.m_logger.error(msg)

    @staticmethod
    def Critical(msg):
        """
         * レベル CRITICAL のログを出力
         * I:  str  msg  出力するメッセージ
        """
        Logger.m_logger.critical(msg)

Logger()
