"""
    OneSignal

    A powerful way to send personalized messages at scale and build effective customer engagement strategies. Learn more at onesignal.com  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: devrel@onesignal.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import onesignal
from onesignal.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_begin_live_activity(self):
        """Test case for begin_live_activity

        Start Live Activity  # noqa: E501
        """
        pass

    def test_cancel_notification(self):
        """Test case for cancel_notification

        Stop a scheduled or currently outgoing notification  # noqa: E501
        """
        pass

    def test_create_app(self):
        """Test case for create_app

        Create an app  # noqa: E501
        """
        pass

    def test_create_notification(self):
        """Test case for create_notification

        Create notification  # noqa: E501
        """
        pass

    def test_create_player(self):
        """Test case for create_player

        Add a device  # noqa: E501
        """
        pass

    def test_create_segments(self):
        """Test case for create_segments

        Create Segments  # noqa: E501
        """
        pass

    def test_delete_player(self):
        """Test case for delete_player

        Delete a user record  # noqa: E501
        """
        pass

    def test_delete_segments(self):
        """Test case for delete_segments

        Delete Segments  # noqa: E501
        """
        pass

    def test_end_live_activity(self):
        """Test case for end_live_activity

        Stop Live Activity  # noqa: E501
        """
        pass

    def test_export_players(self):
        """Test case for export_players

        CSV export  # noqa: E501
        """
        pass

    def test_get_app(self):
        """Test case for get_app

        View an app  # noqa: E501
        """
        pass

    def test_get_apps(self):
        """Test case for get_apps

        View apps  # noqa: E501
        """
        pass

    def test_get_notification(self):
        """Test case for get_notification

        View notification  # noqa: E501
        """
        pass

    def test_get_notification_history(self):
        """Test case for get_notification_history

        Notification History  # noqa: E501
        """
        pass

    def test_get_notifications(self):
        """Test case for get_notifications

        View notifications  # noqa: E501
        """
        pass

    def test_get_outcomes(self):
        """Test case for get_outcomes

        View Outcomes  # noqa: E501
        """
        pass

    def test_get_player(self):
        """Test case for get_player

        View device  # noqa: E501
        """
        pass

    def test_get_players(self):
        """Test case for get_players

        View devices  # noqa: E501
        """
        pass

    def test_update_app(self):
        """Test case for update_app

        Update an app  # noqa: E501
        """
        pass

    def test_update_live_activity(self):
        """Test case for update_live_activity

        Update a Live Activity via Push  # noqa: E501
        """
        pass

    def test_update_player(self):
        """Test case for update_player

        Edit device  # noqa: E501
        """
        pass

    def test_update_player_tags(self):
        """Test case for update_player_tags

        Edit tags with external user id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
