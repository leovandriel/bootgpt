# BootGPT

*Write an application using almost only prompts and a GPT.*

## Usage

Put your OpenAI API key in a file called `key.txt`:

    chmod 600 key.txt

Boot the application builder (might take a minute):

    python -m boot

Run the application builder, e.g. enter "something that writes jokes":

    python -m builder

Run your application:

    python -m app.run

## About

This tools is about building an application for building applications using
natural language and not code. There are plenty GPT-based application writing
tools out there, but they all have a lot of code in them. If writing
applications using natural language is the future, then let's start now.

Consequently, you will find very little code in this repository. It uses a
minimal amount of code to get started and builds from there using natural
language prompts only.

## Booting

`boot.py` is the only Python source file in this project. It forms the start of
a bootstrap sequence that sets up an increasingly capable programming toolchain.

The first step of the boot sequence is recreating `boot.py`. After all, what is
an application to write application if it cannot write itself?

After this `reboot` step, we need to branch out, not to get stuck in a chain of
prompts that can only run prompts to run prompts. Reboot allows us to run
multiple prompts in sequence.

The first of this is a `prompt_runner` source file. This breaks us free from
having to provide detailed instructions on how to call the OpenAI API every time
we want to run a prompt. For every source file we still need two prompts,
because the language model understandably refuses to write python that writes
python.

## Prompting

Use `//` to add comments to prompts that are read by `prompt_runner`

## FAQ

*Why?*

Application building tools like
[gpt-engineer](https://github.com/AntonOsika/gpt-engineer) are showing promise
but still get stuck on relatively simple applications. To understand what is
really needed to write software using a GPT, I want to start from scratch and
understand the fundamental challenges that comes with AI-generated code.

*Why not just write one big prompt that builds the whole application in one go?*

That would be great. Primary reason is that the OpenAI API does not write files
or create projects, it just returns text, so we still need to write code to
transform this text into a folder structure. The whole point of this project is
not to write code, but to use prompts, so we're left with bootstrapping from
much shorter and detailed prompts. Also, I haven't managed to get GPT to write
large amounts of functioning code from a single prompt.

## License

MIT
