import logging
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "amotoori"+time_stamp+"@gmail.com"







