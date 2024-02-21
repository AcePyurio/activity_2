from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
import mysql.connector

# Function to establish a database connection
def connect_to_database():
    return mysql.connector.connect(
        host="db",
        user="root",
        passwd="proot",
        database="restNoteDatabase"
    )

# Function to create the notes table if it doesn't exist
def create_notes_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# Define a handler for processing HTTP requests
class RequestHandler(BaseHTTPRequestHandler):
    # Method to set HTTP headers for the response
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # Handle GET requests
    def do_GET(self):
       # Establish a database connection
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        
        # Retrieve all notes from the database
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()
        
         # Close the cursor and database connection
        cursor.close()
        connection.close()

        # Setting response headers and encoding notes data into JSON
        self._set_headers()
        self.wfile.write(json.dumps(notes).encode('utf-8'))

     # Processing POST requests
    def do_POST(self):
        # Parsing the data length
        content_length = int(self.headers['Content-Length'])
        
        # Reading and parsing raw data into JSON
        post_data = self.rfile.read(content_length)
        note = json.loads(post_data)

        # Inserting new note data into the database
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (note['title'], note['content']))
        connection.commit()
        
        # Closing cursor and connection
        cursor.close()
        connection.close()

        # Sending a 201 Created response with a confirmation message
        self._set_headers(201)
        self.wfile.write(json.dumps({'message': 'created'}).encode('utf-8'))

    # Processing PUT requests
    def do_PUT(self):
        # Parsing the data length
        content_length = int(self.headers['Content-Length'])
        
        # Reading and parsing raw data into JSON
        put_data = self.rfile.read(content_length)
        note = json.loads(put_data)

        # Parsing the note ID from the URL query parameters
        parsed_path = urlparse(self.path)
        note_id = parse_qs(parsed_path.query).get('id', None)

        if note_id:
           # Connecting to the database
            connection = connect_to_database()
            cursor = connection.cursor()

           # Executing the update command
            cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (note['title'], note['content'], note_id[0]))
            connection.commit()
            
            # Closing cursor and connection
            cursor.close()
            connection.close()

            # Sending a success message
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'updated'}).encode('utf-8'))
        else:
           # Sending an error if no note ID provided
            self._set_headers(400)
            self.wfile.write(json.dumps({'message': 'ID is required'}).encode('utf-8'))

    # Processing DELETE requests
    def do_DELETE(self):
        # Parsing the note ID from the URL query parameters
        parsed_path = urlparse(self.path)
        note_id = parse_qs(parsed_path.query).get('id', None)

        if note_id:
            # Establishing a connection to the database
            connection = connect_to_database()
            cursor = connection.cursor()

           # Executing the delete command
            cursor.execute("DELETE FROM notes WHERE id = %s", (note_id[0],))
            connection.commit()

            # Closing the cursor and the connection
            cursor.close()
            connection.close()

           # Responding with a success message
            self._set_headers()
            self.wfile.write(json.dumps({'message': 'deleted'}).encode('utf-8'))
        else:
            # Responding with an error message if no note ID is provided
            self._set_headers(400)
            self.wfile.write(json.dumps({'message': 'ID is required'}).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8010):
    server_address = ('', port)
    
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}...")  
    httpd.serve_forever() 


if __name__ == '__main__':
    
    create_notes_table()
    

    run()