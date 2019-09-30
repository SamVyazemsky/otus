import pytest


@pytest.fixture(scope="module", autouse=True)
def my_own_session_run_at_beginning(request):
    print('\nIn my_own_session_run_at_beginning()')

    def my_own_session_run_at_end():
        print('In my_own_session_run_at_end()')

    yield "my_own_session_run_at_beginning"

    my_own_session_run_at_end()


@pytest.fixture(scope="function")
def some_resource(request):
    print('\nIn some_resource()')

    def some_resource_fin():
        print('\nIn some_resource_fin()')

    request.addfinalizer(some_resource_fin)
