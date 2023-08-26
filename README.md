## Introduction
A demo website built as part of my application to join the JU GDSC Dev team. 

## Tech Used
The backend is a straightforward Flask app with a single route, which uses the response received from the external API to render the Jinja2 template of the frontend.

Bootstrap is used for styling, specifically, a Card component is used for individual conference details.


## Deployment
The app is currently deployed on a DigitalOcean Droplet, and can be accessed [here](gdsc.shakyamajumdar.me).


## Run Locally
To run the project locally, do:
```
$ git clone https://github.com/ShakyaMajumdar/gdsc_recruitment.git
$ cd gdsc_recruitment/
$ poetry install
$ poetry shell
$ flask run
```
Note: You will need [Python](https://www.python.org/downloads/) and [Poetry](https://python-poetry.org/docs/#installation) installed.
