import argparse
import json
import sys
import time

from pynput.mouse import Button, Controller

PARSER = argparse.ArgumentParser(description='')
PARSER.add_argument('--speed', default=1.0, help="How fast to replay events", type=float)
PARSER.add_argument('--step', help="Use a fixed step between actions", type=float, default=None)
PARSER.add_argument('--max-step', help="Maximum pause between events", type=float, default=float("inf"))

def main():
    args = PARSER.parse_args()

    mouse = Controller()
    for line in sys.stdin:
        data = json.loads(line)
        last_seconds = 0
        match data:
            case {"x": x, "y": y, "button": button, "seconds": seconds}:
                step = args.step or min(seconds - last_seconds, args.max_step)
                time.sleep(step / args.speed)
                last_seconds = seconds
                mouse.position = (x, y)
                mouse.press(getattr(Button, button))
                mouse.release(getattr(Button, button))
            case _:
                raise ValueError(data)
