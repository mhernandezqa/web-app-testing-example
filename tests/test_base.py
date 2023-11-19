import pytest


@pytest.mark.usefixtures("chrome_driver_init")
@pytest.mark.usefixtures("login_logout")
class BasicTest:
    
    pass