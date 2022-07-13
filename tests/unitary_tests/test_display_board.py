"""
Tests the /displayBoard url.
"""

from tests.conftest import mock_clubs_and_competitions


def test_display_board(client, mock_clubs_and_competitions):
    response = client.get("/displayBoard")
    data = response.data.decode()
    assert "Display clubs || GUDLFT" and "Clubs:" in data
    assert response.status_code == 200
