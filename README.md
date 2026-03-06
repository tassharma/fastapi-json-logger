# FastAPI JSON Logger

This project is a simple FastAPI application that demonstrates how to configure logging to output JSON-structured logs to stdout.

## Project Structure

```
fastapi-json-logger
├── src
│   ├── main.py        # Entry point of the FastAPI application
│   └── logger.py      # Configures logging to output JSON format
├── requirements.txt    # Lists project dependencies
└── README.md           # Project documentation
```

## Requirements

To run this project, you need to have Python installed. You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI application, navigate to the `src` directory and run:

```
uvicorn main:app --reload
```

This will start the server, and you can access the application at `http://127.0.0.1:8000`.

## Logging

The application includes a `/test-logs` endpoint that logs an INFO message followed by an ERROR message. You can test this endpoint by sending a GET request to:

```
http://127.0.0.1:8000/test-logs
```

You should see the logs output in JSON format in the console.

## License

This project is licensed under the MIT License. Please note the same, we are testing claude pr