#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.

The joke: you decline a meeting, the calendar answers back with a
system message, and the punchline turns the calendar into your boss.
"""
import os

# The line is three beats: decline, the calendar talks back with a
# system message, then the punchline promotes the calendar to boss.
# It won the head-to-head over two other drafts: the reply-all storm
# (funny but a widely told office story) and the fish in the microwave
# (the setup itself is the cliche). This one is the freshest twist,
# clear on one read, and every word earns its place.
# One line, no trailing newline - the gate counts 1 to 200 chars.
LINE = "I declined a meeting invite and the calendar replied, 'The organizer has rescheduled you anyway,' so I now work for the calendar."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the write byte-exact: the line is written as-is,
    # with no trailing newline added and no translation on any platform.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
