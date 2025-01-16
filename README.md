

## Getting Started

### Prerequisites

- Python 3.xx
- Django 5.1.xx
- Virtualenv

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/andresstbn/django_assessment
    cd django_assessment
    ```

2. Create a virtual environment:
    ```sh
    python -m venv env
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

1. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

2. Run the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your browser and go to [http://127.0.0.1:8000/admin](http://_vscodecontentref_/9) to access the Django admin interface (if you need)

    ```
    user: admin 
    password: admin
    ```

### Completing the TODOs

The project contains several TODOs that need to be completed. These TODOs are marked in the code with comments like `# TODO: ...`. Your task is to find and complete all these TODOs to make the project fully functional.
