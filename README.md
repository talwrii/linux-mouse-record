# Linux mouse record
<a href="https://x.com/readwithai">@readwithai</a> - <a href="https://x.com/readwith">X</a> - <a href="https://readwithai.substack.com">substack</a> - <a href="https://www.youtube.com/@readerai">YouTube</a>

A *simple* command-line tool to record and replay mouse *clicks* on Linux.

# Using
```
pipx install linux-mouse-record
linux-mouse-record  > recording.jsonl
linux-mouse-replay < recording.jsonl
# You can also use linux-mouse-replay recording.jsonl
```

The recording file is a stream of JSON lines and can be edited by hand.

# Turning a recording into an executable
If you place:

```
#!/usr/bin/env linux-mouse-replay
```

at the beginning of a recording, and make the recording executable with `chmod +x recording.json`  then you can run the recording from the command-line of from you window manager with a shotcut..

# Demo
![demo](demo.mp4)


# Motivation
I wanted to record a click and replay it. I found a lot of apps, but a lot of them were complicated-to-use GUIs, two didn't work, and a bunch weren't really documented.

This approach will always be be hacky. If you are doing something hard you might like to use a proper form of automation with assestions that check for results. But for something quick and hacky this can work well.

This tool will probably never support additional features you want - unless I need them.

# Alternatives and prior work
This is mostly a wrapper about `pynput`. There are a variety of tools that do this - but I could not find a nice CLI that worked for linux and worked - though perhaps one exists.

# About me
I am <a href="https://x.com/readwithai">@readwithai</a>. I make <a href="https://readwithai.substack.com/">tools</a> for and <a href="https://readwithai.substack.com/">write about</a> <a href="https://readwithai.substack.com/p/reading-and-agency">agency</a> and <a href="https://readwithai.substack.com/p/obsidian-plugin-repl">productivity</a>, particularly related to <a href="https://readwithai.substack.com/p/what-is-reading-broadly-defined">deep reading</a> and for <a href="https://readwithai.substack.com/p/what-exactly-is-obsidian">Obsidian</a>.

If you found this tool useful, perhaps pay me 2 dollars on <a href="https://ko-fi.com/readwithai">kofi</a>.

If that sounds interesting, you can follow me on <a href="https://x.com/readwithai">X</a> or <a href="https://readwithai.substack.com">substack</a>.
