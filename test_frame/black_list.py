# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy


class BlackList:
    __black_list = [(MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.xueqiu.android:id/iv_close']")]

    def get_black_list(self):
        return self.__black_list

    def set_black_list(self, mystype, myvalue=None):
        if myvalue is None:
            self.__black_list.append(mystype)
        else:
            self.__black_list.append((mystype, myvalue))
