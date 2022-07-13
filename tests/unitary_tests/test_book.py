"""
Tests the /book url.
"""

from tests.conftest import mock_clubs_and_competitions


def test_display_booking_htlm_with_valid_competition(
    client, mock_clubs_and_competitions
):
    """
    Tests that booking.html returns with a valid competition.
    """
    response = client.get(
        "/book/Spring Boxing/Iron Temple",
        data={"club": "Iron Temple", "competition": "Spring Boxing", "places": "4"},
    )
    data = response.data.decode()
    assert "Booking for Spring Boxing || GUDLFT" in data
    assert response.status_code == 200
