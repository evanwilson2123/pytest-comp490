import pytest

@pytest.fixture(scope="session")
def foo(request):
    return request.param


@pytest.fixture(scope="session")
def bar(request):
    return request.getfixturevalue("foo")


@pytest.mark.parametrize("foo", [1], indirect=True)
def test_first(foo, bar):
    assert bar == 1


@pytest.mark.parametrize("foo", [2], indirect=True)
def test_second(foo, bar):
    assert bar == 2