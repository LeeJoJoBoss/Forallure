import os
import sys

import pytest

sys.path.append(os.getcwd())
import allure


class Test01():
    #注释
    @allure.step('这是操作步骤1')
    def test01(self):
        allure.attach('最长的电影','')
        allure.attach('备注', '再给我两分钟')
        print('这是测试用例1')

    #注释
    @allure.step('这是操作步骤2')
    def test02(self):
        allure.attach('烟花易冷','')
        allure.attach('备注', '原因')
        print('这是测试用例2')

    # 失败优先级别筛选格式一
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        allure.attach('晴天','')
        allure.attach('备注', '但偏偏风渐渐把距离吹得好远')
        print('这是测试用例3')

    #失败优先级别筛选格式二
    @allure.severity('blocker')
    def test04(self):
        allure.attach('最美的不是下雨天，是猪与你一起躲过的屋檐','')
        allure.attach('备注', '原因')
        print('这是测试用例4')

    #失败执行
    @allure.severity('blocker')
    def test05(self):
        allure.attach('谁得只得那双手，靠拥抱亦难任你拥有','')
        assert 2==3
    #稻香