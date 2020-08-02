import os
text="Hello World"
os.popen( 'espeak "{}" --stdout | aplay 2>/dev/null'.format(text))