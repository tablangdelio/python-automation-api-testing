from http import HTTPStatus
import requests
from config import EnvConfig


class TestUsersAPI:
    api_url = EnvConfig().API_URL

    def test_get_users(self):
        response = requests.get(url=f"{self.api_url}/users", timeout=1)

        response_json = response.json()
        assert response.status_code == HTTPStatus.OK
        assert "page" in response_json
        assert "per_page" in response_json
        assert "total" in response_json
        assert "total_pages" in response_json
        assert "support" in response_json
        assert "data" in response_json
