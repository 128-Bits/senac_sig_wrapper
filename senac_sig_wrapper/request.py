"""
"""
import requests
from senac_sig_wrapper.hooks import check_response_errors


class Request:
    """Request
    A simple request wrapper object specification
    """

    def __init__(self, config=None):
        if not config:
            raise ValueError("Request need configuration values")
        self.__config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.__config.access_token}",
                "Content-Type": "application/json",
            }
        )
        self.session.hooks = {"response": check_response_errors}

    def get(self, url: str = "", *args, **kwargs) -> requests.models.Response:
        """A wrapper for requests.session.get
        """
        return self.session.get(
            url=f"{self.__config.base_url}{url}", *args, **kwargs
        )

    def post(
        self, url: str = "", data: dict = {}, **kwargs
    ) -> requests.models.Response:
        """A wrapper for requests.session.post

        """
        return self.session.post(url=f"{self.__config.base_url}{url}", data=data, **kwargs)

    def delete(self, url: str = ""):
        """A wrapper for requests.Session.delete
        """
        return self.session.delete(url)

