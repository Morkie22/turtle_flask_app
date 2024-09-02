from flask import Flask, render_template, request
from turtle import Screen, Turtle
import threading

# Initialize Flask app
app = Flask(__name__)

# Global variables for the Turtle graphics
screen = None
t = None

# Function to set up the Turtle screen and the Turtle object
def setup_turtle():
    global screen, t
    screen = Screen()
    t = Turtle()
    screen.title("Turtle Control")
    screen.setup(width=800, height=600)

# Function to execute Turtle commands safely using the screen's ontimer method
def execute_turtle_command(command):
    # Use the screen's ontimer to ensure commands are executed within the main loop
    if command == 'forward':
        screen.ontimer(lambda: t.forward(50), 0)
    elif command == 'backward':
        screen.ontimer(lambda: t.backward(50), 0)
    elif command == 'left':
        screen.ontimer(lambda: t.left(45), 0)
    elif command == 'right':
        screen.ontimer(lambda: t.right(45), 0)
    elif command == 'clear':
        screen.ontimer(lambda: t.clear(), 0)

# Route to render the main control page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle Turtle commands from the form buttons
@app.route('/move', methods=['POST'])
def move():
    command = request.form.get('command')
    execute_turtle_command(command)  # Execute the command received from the button click
    return '', 204

# Function to run the Flask server in a separate thread
def run_flask():
    app.run(use_reloader=False, debug=True)

# Main function to initialize the Turtle graphics and Flask server
def main():
    # Initialize the Turtle setup
    setup_turtle()

    # Start the Flask app in a separate thread to keep it running alongside Tkinter
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start the Tkinter main loop to keep the Turtle graphics active
    screen.mainloop()

if __name__ == '__main__':
    main()

