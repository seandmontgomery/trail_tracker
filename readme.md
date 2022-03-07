![Trail Tracker](website/static/images/read-me-logo.png "Trail Tracker")

by [Sean Montgomery](https://www.linkedin.com/in/seandmontgomery/) | [seandmontgomery@gmail.com](mailto:seandmontgomery@gmail.com?subject=[GitHub]%20Trail_Tracker)

## <a name="#About"></a>What is Trail Tracker?
Trail Tracker - is a comprehensive full stack web application for hiking enthusiasts. This application allows users to store information and media for all of their favorite hikes while also compiling data and displaying their statistics.

![DemoGIF]()

Table of Contents
------
- [Tech Stack](#Tech)
- [Features](#Features)
- [Install](#Install)
- [Meet the Developer](#Meet)
- [Looking Ahead](#Future)

## <a name="#Tech"></a>Tech Stack

- **Frontend**: JavaScript | HTML5 | CSS | Bootstrap
- **Backend**: Python3 | Flask | SQLAlchemy | Jinja2
- **APIs**: Cloudinary | GoogleMaps
- **Database**: PostgreSQL

## <a name="#Features"></a>Features
[Login](#Login) | [Timeline](#Timeline) | [Location](#Location) | [View](#View) | [Search](#Search) | [Upload](#Upload) | [Logout](#Logout) | [Database](#SQLDBM)

## <a name="#Login"></a>Login and Registration
Users can register and create an account which will give them access to their personal trail logs. I have hashed the user's credentials with sha256 to add security for the user. I built Trail Tracker with Flask - creating a service that uses a Postgres database interfaced with the SQLAlchemy ORM.

![Login]()

## <a name="#Timeline"></a>Timeline
Styled using Bootstrap and CSS. This information is being dynamically displayed using Jinja templating.

![Timeline]()

## <a name="#Location"></a>Location
Clicking on the "location" button opens Google Maps to show exactly where the trail is located.

![Location]()

## <a name="#Notes"></a>View Image
Notes

![Notes]()

## <a name="#Search"></a>Search
To filter through the cards, I developed a search feature by adding a JavaScript event listener that evaluates keystrokes to hide the cards that do not contain text matching the query string.

![View]()

## <a name="#Upload"></a>Upload Image
To upload...  and the location using Google’s Map & Places API with their Place Autocomplete service. For the image files itself I implemented Cloudinary’s media management API, which returns the url for the image uploaded to my database.

![Upload]()

## <a name="#Logout"></a>Log Out
![Logout]()

## <a name="#Data"></a>Data Model

![SQLDBM]()

## <a name="#Future"></a>Looking Ahead
Thank you for taking the time to learn a bit about Trail Tracker, I really look forward to connecting with you!

## <a name="#Install"></a>Install

### Running Trail Tracker

1. Clone this repository:
```shell
git clone 
```

***Optional***: Create and activate a virtual environment:
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

2. Install dependencies: 
```shell
pip3 install -r requirements.txt
```

3. Create environmental variables to hold your API keys in a `secrets.sh` file. You'll need to create your own Cloudinary API keys:
```
export cloud_name="create your own cloudindary name/account"
export cloud_api_key="once you do this they will provide you a key which you will put here"
export cloud_api_secret="use your own secret of course, shhh"
```

4. Create your database:
```shell
createdb trail_tracker
```

5. Run the app on localhost:
```shell
python3 main.py
```

## <a name="#Meet"></a>Meet the Developer
My background in entertainment and education has lead me down a new creative path into tech. I am a skilled full stack web developer with a passion for multimedia presentation. I am proficient in the following technologies: Python, Javascript, AJAX, JSON, HTML, CSS, SQL, Flask, jQuery, Bootstrap, Jinja, SQLAlchemy, PostgreSQL, Command Line, Git, GitHub, and Agile. As a multimedia creator I am skilled in the following applications: Camtasia, Adobe Premiere Pro, iMovie, Garage Band, Descript, Snagit, and Canva. I have also had a successful 15 year career as a professional broadway actor in NYC. In my free time I enjoy mountain biking, hiking, snowboarding, running, cooking and international travel.

Connect with [Sean Montgomery](https://www.linkedin.com/in/seandmontgomery/) on LinkedIn!