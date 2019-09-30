import allure
# --allure-epics
#
# --allure-features
#
# --allure-stories
#
# for example:
#
# $ pytest tests.py --allure-stories story_1,story_2
#
# collected 5 items
#
# tests.py ...                                                                    [100%]
#
# ============================== 3 passed in 0.01 seconds ==============================
# $ pytest tests.py --allure-features feature2 --allure-stories story2
#
# collected 5 items
#
# tests.py ...


def test_without_any_annotations_that_wont_be_executed():
    pass


@allure.story('epic_1')
def test_with_epic_1():
    pass


@allure.story('story_1')
def test_with_story_1():
    pass


@allure.story('story_2')
def test_with_story_2():
    pass


@allure.feature('feature_2')
@allure.story('story_2')
def test_with_story_2_and_feature_2():
    pass
