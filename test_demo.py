import pytest
def test_firstProgram():
    print("Hello hhCgyjg hinmaya")
    print("chinmkuku")
    print("Hello GitHub")


@pytest.mark.usefixtures("browser")
def test_browser(browser):
    print(browser)