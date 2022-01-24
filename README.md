# Challenge Calyx

This is the repository where the solution to the Calyx challenge is hosted.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the bot and how to install them
1. Download and install Python 3. You can download from https://www.python.org/downloads/

2. Create an enviorment to run the script properly

    ```
    python -m venv /path/to/new/virtual/environment
    ```
    Then, activate it:
    ```
    path_env\venv\Scripts\activate
    ```    
3. You have to install dependencies that ```requirements.txt``` contains.

    ```
    pip install -r requirements.txt
    ```

4. Create a copy of your .env file

    ```
    cp .default.env .env
    ```
5. Config your .env 
    ```
    USER=user
    PASSWORD=pwd
    HOSTNAME=localhost
    PORT=5432
    DB_NAME=instituciones
    ```

### Running script

You only have to run the main.py file:

```
python3 main.py
```

## Built With

- [requests](https://docs.python-requests.org/en/latest/) - Requests is a simple, yet elegant, HTTP library.
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper.
- [pandas](https://pandas.pydata.org/) - pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive.
- [lxml](https://lxml.de/) - The lxml XML toolkit is a Pythonic binding for the C libraries libxml2 and libxslt.
- [python-decouple](https://github.com/henriquebastos/python-decouple/) - Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.
## Author

- **Nicolás Liendro** - _Initial work_ - [GitLab](https://gitlab.com/NicoLiendro14),
  [GitHub](https://github.com/NicoLiendro14),
  [GitHub2](https://github.com/NicoLiendro10) and
  [LinkedIn](https://www.linkedin.com/in/nicolas-liendro/)