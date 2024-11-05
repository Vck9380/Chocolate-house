Chocolate House Management Application

Requirements
- Python 3.9 or later(3.12.6)
- Docker (for running the application in a container)

Methods for running the Application
1.Clone the repository

```bash
git clone <repository-url>
```

2.Running locally (without Docker)

```bash
pip install -r requirements.txt
python main.py
```

3.Running with Docker

- Build the Docker image:
  ```bash
  docker build -t chocolate_house .
  ```

- Run the container:
  ```bash
  docker run -p 8000:80 chocolate_house
  ```

Features of project
- Add and view seasonal flavors
- Manage ingredient inventory
- Accept customer flavor suggestions with allergy concerns


Sqlalchemy is used in place of sqllite as it is more flexible and since we use ORM abstaction