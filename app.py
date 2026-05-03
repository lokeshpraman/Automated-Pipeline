# We import Flask from the library we just installed.
from flask import Flask

# This line creates the actual application.
# '__name__' tells Flask where to look for files behind the scenes.
app = Flask(__name__)

# This is a "decorator". It tells the server: "If a user visits the root
# URL (like www.yourwebsite.com/), run the function directly below this line."
@app.route('/')
def home():
    # This is a basic return statement. Whatever is returned here is exactly
    # what gets printed on the user's screen.
    return "Pipeline Active: V2 Deployed via CI/CD!"

# This block checks if you are running the script directly.
# If you are, it starts the web server on port 5001.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)