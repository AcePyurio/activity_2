### Introduction:

This project aims to develop a RESTful API for a simple note-taking application. The API allows users to perform CRUD operations (Create, Read, Update, Delete) on notes stored in a MySQL database. With endpoints designed to handle these operations, the API provides a backend solution for managing notes efficiently. This project focuses on implementing core functionality using Python's built-in HTTP server module and Docker for containerization, offering a lightweight and scalable solution for note management.

---

### Installation Guide:

#### Dependencies:

- Docker installed on your machine.

#### Setup Instructions:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AcePyurio/activity_2_.git
   ```
   This command clones the project repository from the specified URL.

2. **Navigate to the project directory:**
   ```bash
   cd project-directory
   ```
   Use this command to change your current directory to the project directory where you cloned the repository.

3. **Build the Docker containers:**
   ```bash
   docker-compose build
   ```
   This command builds the Docker containers defined in the `docker-compose.yml` file. It pulls the necessary images and installs dependencies specified in the Dockerfile.

4. **Start the Docker containers:**
   ```bash
   docker-compose up
   ```
   Running this command starts the Docker containers as defined in the `docker-compose.yml` file. It starts both the MySQL database and the API server containers.

5. **Access the API server:**
   Once the containers are up and running, the API server should be accessible at `http://localhost:8010`. You can now interact with the API endpoints using tools like Postman or cURL.

---
### API Documentation:

#### Endpoints:

 **GET /notes**
   - **Description**: Retrieves all notes stored in the database.
   - **Request Method**: GET
   - **Response Format**: JSON
   - **Example Response**:
     ```json
     [
       {
         "id": 1,
         "title": "Note 1",
         "content": "Content of note 1"
       },
       {
         "id": 2,
         "title": "Note 2",
         "content": "Content of note 2"
       }
     ]
     ```

 **POST /notes**
   - **Description**: Creates a new note in the database.
   - **Request Method**: POST
   - **Request Body Format**: JSON
   - **Example Request**:
     ```json
     {
       "title": "New Note",
       "content": "Content of the new note"
     }
     ```
   - **Example Response**:
     ```json
     {
       "message": "created"
     }
     ```

 **PUT /notes?id={note_id}**
   - **Description**: Updates an existing note in the database.
   - **Request Method**: PUT
   - **Request Body Format**: JSON
   - **Example Request**:
     ```json
     {
       "title": "Updated Note",
       "content": "Updated content of the note"
     }
     ```
   - **Example Response**:
     ```json
     {
       "message": "updated"
     }
     ```

 **DELETE /notes?id={note_id}**
   - **Description**: Deletes a note from the database based on its ID.
   - **Request Method**: DELETE
   - **Example Request**:
     ```http
     DELETE /notes?id=1
     ```
   - **Example Response**:
     ```json
     {
       "message": "deleted"
     }
     ```

---

### Usage Guide:

#### Starting the Application:<br>

 **Build and run the Docker containers**:<br>
   - Follow the installation guide to build and run the Docker containers for the project.

#### Interacting with the API:<br>

 **Testing API Endpoints using Postman**:
    Open Postman and import the provided collection file.
    Ensure that the Docker containers are running.
   
 **GET /notes**:<br>
    Send a GET request to `http://localhost:8010/notes` to retrieve all notes.
    Example:
     http
     GET http://localhost:8010/notes
     
   
 **POST /notes**:<br>
    Send a POST request to `http://localhost:8010/notes` with a JSON body containing the title and content of the new note.
    Example:
     http
     POST http://localhost:8010/notes
     Content-Type: application/json

     {
       "title": "New Note",
       "content": "Content of the new note"
     }
     

 **PUT /notes?id={note_id}**:<br>
    Send a PUT request to `http://localhost:8010/notes?id={note_id}` with a JSON body containing the updated title and content of the note, and specify the `note_id` to update.
    Example:
     http
     PUT http://localhost:8010/notes?id=1
     Content-Type: application/json

     {
       "title": "Updated Note",
       "content": "Updated content of the note"
     }
     

 **DELETE /notes?id={note_id}**:<br>
    Send a DELETE request to `http://localhost:8010/notes?id={note_id}` to delete the note with the specified `note_id`.
    Example:
    http
     DELETE http://localhost:8010/notes?id=1
    

---


### Supplementary Details:
- The Dockerfile sets up the Python environment and copies the application code, while the docker-compose.yml defines services for the MySQL database and the API server.
- The MySQL database table `notes` consists of three fields: `id`, `title`, and `content`.

---

### Contributors:
- **John Paul Alvarez**: Creator and developer of the project. Implemented the RESTful API, database integration, Docker setup, and documentation.
