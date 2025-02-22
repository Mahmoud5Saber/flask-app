from flask import Flask, render_template, jsonify
import logging
import os

app = Flask(__name__)  # Create the main Flask app object

# Home page route
@app.route("/")
def home():
    return render_template("index.html")  # Renders the homepage template

# Test API route (returns JSON instead of HTML)
@app.route("/api")
def api():
    return jsonify({"message": "This is a test API", "status": "success"})

# 404 Error handler with logging
logging.basicConfig(level=logging.INFO)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.info(f"Page not found: {error}")
    return render_template("404.html"), 404

# Run the app locally at port 5050 with configurable debug mode
if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='127.0.0.1', port=5050, debug=debug_mode)
