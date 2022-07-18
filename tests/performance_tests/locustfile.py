from locust import HttpUser, task, between


class ProjectPerfTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def home(self):
        self.client.get("/")

    @task
    def logout(self):
        self.client.get("/logout")

    @task
    def show_summary(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})

    @task
    def display_board(self):
        self.client.get("/displayBoard")

    @task
    def display_competitions(self):
        self.client.get("/book/Fall Classic/Simply Lift")

    @task
    def purchase_places(self):
        self.client.post(
            "/purchasePlaces",
            {"places": "2", "club": "Simply Lift", "competition": "Fall Classic"},
        )
