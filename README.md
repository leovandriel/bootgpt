<img src="logo.jpg" width="25%" height="25%" align="right" alt="bootGPT logo">

# bootGPT

Writing an application writer using almost only prompts and an LLM, learning about
coding with LLMs along the way.

## Usage

Before we start, a quick disclaimer: *The following will indiscriminately
execute code generated by `gpt-3.5-turbo` on your machine, without your review,
and with potentially undesired consequences.*

Put your OpenAI API key in a file called `key.txt`:

    chmod 600 key.txt

Boot the application builder (might take a minute):

    python -m boot

Run the application builder, e.g. enter "something that writes jokes":

    python -m builder

Run your application:

    python -m app.run

## About

This tools is about building software for building software using natural
language, not code. There are plenty GPT-based application writing tools out
there, but they are built with human-written code. If writing applications using
natural language is the future, then let's start now.

Consequently, you will find very little code in this repository. It uses a
minimal amount of code to get started and builds from there using natural
language prompts only.

## Booting

`boot.py` is the only Python source file in this repository. It forms the start
of a bootstrap sequence that sets up an increasingly capable programming
toolchain.

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
really needed to write software using a GPT, we'll start from scratch and
understand the fundamental challenges that come with AI-generated code.

*Why not just write one big prompt that builds the whole application in one go?*

That would be great. The primary reason is that the OpenAI API returns text (and
calls functions), but does not write complex applications, so we still need to
write code to transform model output into our application and guide it along the
way. The whole point of this project is not to write code, but to use prompts,
so we're left with bootstrapping from shorter and instructive prompts.

Secondly, we haven't managed to get GPT to write large amounts of functioning
code from a single prompt. It will likely get there, and as it gets closer we
incrementally simplify the boot prompts.

*Isn't this just an painful way to write mediocre code?*

For now it is.

## License

MIT
