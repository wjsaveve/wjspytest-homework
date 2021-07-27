# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class BlackList:
    __black_list = [(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn")]

    def get_black_list(self):
        return self.__black_list

    def set_black_list(self, mystype, myvalue=None):
        if myvalue is None:
            self.__black_list.append(mystype)
        else:
            self.__black_list.append((mystype, myvalue))
