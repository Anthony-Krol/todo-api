# Todo API

A simple, efficient, and secure Todo API built with FastAPI, SQLAlchemy, and OAuth2 for authentication.

## Project Description

This project provides a RESTful API for managing todo items. Users can register, log in, create, read, update, and delete their todo items. The API uses OAuth2 for authentication and token management.

## Features

- User Registration and Authentication
- CRUD operations for Todo items
- OAuth2 for secure access
- SQLAlchemy ORM for database interactions
- Token-based authentication

## Installation

To get started with this project, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anthony-Krol/todo-api.git
   cd todo-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - The project uses SQLite by default, no additional setup is required.

5. **Create the database tables**:
   ```bash
   python -c 'from database import Base, engine; Base.metadata.create_all(bind=engine)'
   ```

6. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

### API Endpoints

![image](https://github.com/Anthony-Krol/todo-api/assets/152611744/9981dad1-1bd3-4977-8cec-ecd57bbc2fc1)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out via [antoni.krol@edu.uni.lodz.pl](mailto:antoni.krol@edu.uni.lodz.pl).

