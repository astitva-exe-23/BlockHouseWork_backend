
# ProjectFinal Backend

## Overview
. Follow these instructions to set up and run the backend server.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (recommended)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/projectfinal.git
cd projectfinal/backend
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. 

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Create and apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```



Follow the prompts to enter your username, email, and password.

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start and you can access the backend at `http://127.0.0.1:8000/`.


## API Endpoints

- **GET /api/line-chart-data/**: Fetch data for the line chart.
- **GET /api/pie-chart-data/**: Fetch data for the pie chart.
- **GET /api/candlestick-chart-data/**: Fetch data for the candlestick chart.




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

