# PizzaPal

PizzaPal is a Python application designed to streamline the process of managing toppings and pizza recipes.

## Getting Started

A demo instance of PizzaPal is available at <https://pizzapal.aprilsigda.com>. Two users have already been created for the demo: a pizza chef account with the username 'chef' and password 'chef', and a manager account with the username 'manager' and password 'manager'.

To run PizzaPal on your local machine, follow these steps:

1. Install Python 3 and Pip.
2. Clone this repository and navigate to its root directory with the following commands:

        git clone https://github.com/aprilsigda/pizzapal
        cd pizzapal

3. (Optional but recommended) Install the Python venv module, create a virtual environment, and activate it:

        python -m venv venv
        source ./venv/bin/activate

4. Install the project's dependencies with Pip:

        pip install -r requirements.txt

5. Launch the application:

        flask run

If everything completed successfully, the application will be listening on <http://localhost:5000>.

## Usage

When loading PizzaPal, you are presented with a login screen. To add a user, use the 'Signup' link in the top right corner. After signing in to the application, you will see either the Manage Toppings page or the Manage Pizzas page, depending on whether you are logged in as a manager or a chef. On these pages, you can view, edit, and delete existing toppings and pizzas, and you can create new ones.

## Technical choices

When developing this application, I chose to use Python with Flask as the backend framework. Flask is an excellent framework for creating web applications, and it is one that I was already familiar with which made it an easy choice. On the frontend, I used Bootstrap to style the interface components. I chose Bootstrap for its simplicity and ease of use. The backend database runs on SQLite, but because I used SQLAlchemy as an interface it would be trivial to swap out the backend for a different SQL server. The demo is hosted on a Google Cloud Compute VM, which I chose because its free plan is sufficient to host a simple web app.