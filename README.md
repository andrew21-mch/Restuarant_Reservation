# Restuarant_Reservation
![landing page](images/landing.png?raw=true "Title")
This is a potfolio project from alx students that will help reserve local dishes and/or seats for customer for registered restuarants.
* Linkt to blog artilce: https://machinda.hashnode.dev/restaurant-reservation-web-application-foodie
* Deployed site: (for now follow the instructions to run locally)  https://github.com/Nicodona/Restuarant_Reservation
Authors LinkedIn: 
- Nfon Andrew(https://www.linkedin.com/in/nfon-andrew-7703a11a0/)
- Njei Nicodemus(https://www.linkedin.com/in/njei-nicodemus-281a7b1b3/)
- Lukong Anne (https://www.linkedin.com/in/lukong-anne/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Clone the project

```
git clone https://github.com/Nicodona/Restuarant_Reservation
```

### Prerequisites

Reqirements for the project

```
asgiref==3.5.2
Django==4.1.3
django-environ==0.9.0
django-rest-framework==0.1.0
djangorestframework==3.14.0
Pillow==9.3.0
pytz==2022.6
sqlparse==0.4.3
tzdata==2022.6
```

### Installing

To Install the above requirements

```
pip install -r requirements.txt
```

## Running Migrations

To run migrations

```
python manage.py makemigrations
python manage.py migrate
```

## Starting the server

To start the server

```
python manage.py runserver
```

## Usage
* Foodie is used by Restaurant owners to showcase their restaurant on the application as well as display thier menu.
* Foodie is used by User's to book food from a restaurant and can as well reserve seats.


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap5](https://www.getbootstrap.com/) - The CSS framework used
We used Django for our project because we were comfortable with it even though not everyone but as a team we worked to make the problem be what it is. 
We equally used the Bootstrap to ease us with our styling. This was a challenge to some of us but with effort it was possible.A

## Feautures
![signup page](images/signup.png?raw=true "Title")
* Login and Registration was implemented
* There was the possibility to search for food.

## Authors

* **Nicodona** - *Initial work* - [Nicodona](https://github.com/Nicodona)
* **Lukong123** - *Initial work* - [Lukong123](https://github.com/Lukong123)
* **Andrew21-mch** - *Initial work* - [Andrew21-mch](https://github.com/Andrew21-mch)

## Related projects
* https://eatapp.co/
* https://www.kayak.com/restaurants

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

To contribute to this project, follow the steps below:

* Fork the project repository by clicking on the Fork button on the top of the page. This will create a copy of this repository in your account.

* Clone the forked repository to your machine by running the following command on your terminal:

```bash
git clone
```

* Create a new branch for the new feature you want to add by running:

```bash
git checkout -b <branch-name>
```

* Make your changes and commit them by running:

``` bash
git add .
git commit -m "commit message"
```

* Push your changes to your remote repository by running:

``` bash
git push origin <branch-name>
```

* Open a pull request on the original repository by clicking on the `New pull request` button on your forked repository.

* Wait for your changes to be reviewed and merged.

