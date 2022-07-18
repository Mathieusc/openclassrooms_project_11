"""
Testing without mock data.
"""


def test_show_summary_with_existing_email(client):
    email = "john@simplylift.co"
    response = client.post("/showSummary", data={"email": email}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "john@simplylift.co" in data


def test_show_summary_with_non_existing_email(client):
    email = "non_existing@mail.com"
    response = client.post("/showSummary", data={"email": email}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "This email does not exist." in data
