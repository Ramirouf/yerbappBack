# Research Project Management API

This project is a backend API designed to facilitate the management of research projects, focusing on data collection, storage, and analysis. Built with FastAPI, it ensures high performance and scalability, catering to the needs of researchers and project managers.

## Features

- **User Authentication**: Secure user registration and authentication mechanisms.
- **Project Management**: Create, update, and manage research projects efficiently.
- **Data Handling**: Robust endpoints for data collection and retrieval.
- **Role-Based Access Control**: Implementing the "investigador" role with comprehensive access permissions.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Docker**: Containerization platform to streamline development and deployment.
- **pgAdmin**: A web-based interface for managing PostgreSQL databases.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Python 3.10**: The project is built using Python 3.10.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ramirouf/yerbappBack.git
   cd yerbappBack
    ```

2. **Set Up Environment Variables:**

Create a .env file in the project root directory with the following content:

POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin_password
SECRET_KEY=your_secret_key

Replace placeholders with your actual credentials.

3. **Build and Run Docker Containers:**

docker compose up --build

This command will set up the PostgreSQL database and pgAdmin interface.

4. **Apply Database Migrations:**

Ensure all necessary database migrations are applied.

5. **Access the API Documentation:**

Once the server is running, navigate to http://localhost:8000/docs to explore the interactive API documentation.

Usage
- Authentication: Register a new user or log in using existing credentials to obtain an authentication token.
- Project Operations: Use the provided endpoints to create, read, update, or delete research projects.
- Data Management: Submit and retrieve research data associated with specific projects.