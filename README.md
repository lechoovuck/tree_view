# Setup

## Prerequisites

- Python 3.10 or later
- `pip` (Python package installer)

## Steps

### 1. Clone the Repository

If you are starting from an existing repository, clone it using:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

Replace `https://github.com/your-username/your-repository.git` with the URL of your repository.

### 2. Create and Activate a Virtual Environment

Creating a virtual environment isolates your project’s dependencies from other projects.

#### On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

Once the virtual environment is activated, install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes Django and any other dependencies.

### 4. Start the Development Server

Start the Django development server with:

```bash
python manage.py runserver
```

The server will start on `http://127.0.0.1:8000/`. You can access it from your web browser.

### 5. Access the Admin Interface (Optional)

If you created a superuser, you can access the admin interface at `http://127.0.0.1:8000/admin/` with _admin/admin_.

## Troubleshooting

- If you encounter issues with package installations, ensure your virtual environment is activated.
- If `python` is not recognized, use `python3` instead.
