import pytest


@pytest.mark.env("stage1")
def test_basic_db_operation():
    print('Test result')

    
@pytest.mark.env("stage1")
@pytest.mark.env("stage2")
def test_basic_db_operation_ex():
    print('Test result')
# pytest -E stage2
# pytest -E stage1
