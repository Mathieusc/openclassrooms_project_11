import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = ""
    try:
        club = [club for club in clubs if club["email"] == request.form["email"]][0]
        return render_template("welcome.html", club=club, competitions=competitions)
    except IndexError:
        flash("This email does not exist.")
        return render_template("index.html")


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    MAX_PLACES = 12
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    date_competition = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    if placesRequired > int(club["points"]):
        flash("Your club does not have enough points to participate.")
    elif placesRequired > MAX_PLACES:
        flash("You cannot book more than 12 places.")
    elif datetime.now() > date_competition:
        flash("Purchase not allowed - Outdated competition.")
    else:
        competition["numberOfPlaces"] = (
            int(competition["numberOfPlaces"]) - placesRequired
        )
        club["points"] = int(club["points"]) - placesRequired
        flash("Great-booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/displayBoard", methods=["GET"])
def display_board():
    return render_template("display_board.html", clubs=clubs)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
