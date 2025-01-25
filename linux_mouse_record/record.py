import json
import time

import pynput.mouse


class Handlers:
    def __init__(self):
        self.start = time.time()

    def on_click(self, x, y, button, pressed):
        seconds = time.time() - self.start
        if pressed:
            print(json.dumps(dict(seconds=seconds, x=x, y=y, button=button.name)))

handlers = Handlers()
with pynput.mouse.Listener(on_click=handlers.on_click) as listener:
    listener.join()
