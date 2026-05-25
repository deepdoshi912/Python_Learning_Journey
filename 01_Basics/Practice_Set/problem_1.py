#PROBLEM-1: Install an external module and use it to perform an operation of your Interest.

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hey Deep! I Know you are learning Python and you are doing great! Keep it up!")
engine.runAndWait()