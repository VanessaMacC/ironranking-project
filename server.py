from src.app import app
import src.controllers.student_controller
import src.controllers.lab_controller

from config import PORT

app.run("0.0.0.0", PORT, debug=True)