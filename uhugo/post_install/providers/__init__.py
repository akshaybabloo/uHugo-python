import os
from typing import Text


class ProviderBase:
    """
    This is a base class for all the providers
    """

    def __init__(self, api_key: Text = None, config_path: Text = None, hugo_version: Text = None):
        """

        :param hugo_version: New Hugo version
        :param api_key: Authentication key for providers
        :param config_path: Path for configuration file of the provider
        """
        self.hugo_version = hugo_version
        self.api_key = api_key
        self.path = config_path

        if not self.api_key:
            self.api_key = os.environ.get("UHUGO_KEY", None)

        if not self.path:
            self.path = os.environ.get("UHUGO_CONFIG_PATH", None)

        if not self.hugo_version:
            self.hugo_version = os.environ.get("HUGO_VERSION", None)

        if not self.api_key and not self.path and not self.hugo_version:
            raise ValueError("api_ky, config_path or hugo_version not set")

    def update_api(self, project_name: Text = None):
        """
        Updates an API
        :return:
        """
        pass

    def update_file(self):
        """
        Updates a configuration file

        :return:
        """
        pass

    def get_projects(self, project_name: Text = None) -> Any:
        """
        Checks and gets the current project

        :param project_name: Name of the project to update
        """
        pass
