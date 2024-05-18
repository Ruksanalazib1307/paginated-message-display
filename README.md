# Paginated Message Display 

# Paginated Message Display

A Django project to fetch, display, and paginate messages with their sources from an external API.

## Features

- Fetches messages and their sources from an external API.
- Displays messages with pagination.
- Handles errors gracefully.

## Requirements

- Python 3.7 or higher
- Django 3.2 or higher
- requests library

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ruksanalazib1307/paginated-message-display.git
    cd paginated-message-display
    ```

2. **Set up a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

- `fetch_citations.py`: Contains the function to fetch data from the API and identify citations.
- `beyondchats/`: Django project directory containing settings and main configuration.
- `citations/`: Django app handling the citation-related logic and views.
- `templates/citations.html`: HTML template for displaying messages.

## Usage

- **API Endpoint:** `http://127.0.0.1:8000/citations/get_citations/`
- **Web Interface:** `http://127.0.0.1:8000/`

## Error Handling

The project includes error handling for API requests and JSON parsing. Errors are logged and returned as JSON responses with appropriate status codes.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


