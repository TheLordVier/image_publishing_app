## Image publishing app (small API for publishing posts with images, text and comments to them)

Project developed by: Mikhailov Alexander

---

**Application structure:**:

 - .github/workflows - directory that contains the configuration files for GitHub Actions
 - data - JSON files with posts, comments and bookmarks data
 - logs - log file
 - static - CSS and image files
 - templates - HTML templates for API
 - test - test classes for API
 - .dockerignore - files and folders to ignore in Docker
 - .gitignore - files and folders to ignore in Git version control
 - app - main Flask application file with views
 - config - application constants
 - db.py - creating a SQLAlchemy database
 - docker-compose.yaml - configuration file for Docker Compose (local)
 - docker-compose-ci.yaml - configuration file for Docker Compose (CI/CD)
 - Dockerfile - container image file
 - flask-app.service - service file that manages starting, stopping, and controlling the background execution of the Flask app
 - logger.py - logger for API
 - utils.py - file with functions for API
 - requirements.txt - application dependencies

--- 

 **The application implements the following features:**:
 - Home page with loading of all posts from JSON file
 - Single post page with detailed content and comments to it
 - Keyword search page
 - Custom posts page with all the posts posted by the user
 - Tags page with posts found by tags
 - Bookmarks page with user-saved posts downloaded from JSON file
 
---

**How to start the project:**
 - Clone the repository
 - Install python and another base requirements such as pip and python3-venv
 - Create and activate the virtual environment `python3 -m venv venv` and `. venv/bin/activate` (for Linux)
and `venv\Scripts\activate` (for Windows).
 - Install the requirements with the `pip install -r requirements.txt` command.
 - Run the app by the command `python app.py`
 - The application is now ready to run