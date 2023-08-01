"""
    OneSignal

    A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com  # noqa: E501

    The version of the OpenAPI document: 1.2.2
    Contact: devrel@onesignal.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import onesignal
from onesignal.model.identity_object import IdentityObject
from onesignal.model.properties_object import PropertiesObject
from onesignal.model.subscription_object import SubscriptionObject
from onesignal.model.user_subscription_options import UserSubscriptionOptions
globals()['IdentityObject'] = IdentityObject
globals()['PropertiesObject'] = PropertiesObject
globals()['SubscriptionObject'] = SubscriptionObject
globals()['UserSubscriptionOptions'] = UserSubscriptionOptions
from onesignal.model.user import User


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """Test User"""
        # FIXME: construct object with mandatory attributes with example values
        # model = User()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
