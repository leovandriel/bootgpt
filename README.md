<img src="logo.jpg" width="25%" height="25%" align="right" alt="bootGPT logo">

# bootGPT

Writing an application writer using almost only prompts and an LLM, learning
about coding with LLMs along the way.

## Usage

Before we start, a quick disclaimer: *The following will indiscriminately
execute code generated by `gpt-3.5-turbo`, on your machine, without your review,
and with potentially undesired consequences.*

Install the openai package:

    pip install openai

Put your OpenAI API key in a file called `key.txt`:

    chmod 600 key.txt

Boot the application builder (might take a minute):

    python -m boot

Run the application builder, e.g. enter "something that writes jokes":

    python -m builder

Run your application:

    python -m app.run

Doesn't work? See [Troubleshooting](#troubleshooting)

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

The second is `prompt_runner_cache`, which adds basic caching capabilities in
order to speed access to the LLM. This simply appends to the existing source
file, requiring a reload of the module.

Lastly, reboot runs the `main` prompt, which is the main sequence of
bootstrapping prompts. By splitting this out of reboot, we have access to the
functionality we defined in the above prompts, like prompt comments.

## Caching

To iterate fast, we cache all API calls early in the bootstrap process, using a
very basic cache that writes to the `cache` folder with the md5sum of the prompt
as filename, and .py extension.

The exception are the early boot prompts, up to the `main` prompt. After the
first boot run, you can use main.py for all subsequent boots, unless you modify
any of the prompts that run before main:

    python -m main

The cache does not invalidate. In order to purge the cache, run:

    rm -rf cache

## Prompting

Use `//` to add comments to prompts that are read by `prompt_runner`

## Troubleshooting

There is a good chance that it throws an error or otherwise doesn't work as
expected. For the same input, the GPT model does not always write the same code.
On top of that, this tool still have many imperfections.

If the `boot` run fails, you probably get a stack trace with very little
information in it. This is because we use the `exec` function to run code and
there are no python sources to point to. To see the code is executed, modify the
suspected prompt by inserting a line that says something like "Print it", right
before "Run using exec".

The prompt runner looks for the `--verbose` flag (`-v`) to print the output of
the model. This can be helpful for getting context for a error message:

    python -m boot --verbose
    python -m main --verbose

If the `builder` run fails, there is probably a bug in the generated source
code. Old-fashioned debugging is possible at this point, see sources in `src/`.
To generate better sources, prompts will need to be engineered. Consider posting
an issue in GitHub, including the generated sources.

If `app.run` does not have the desired behavior, then that is probably because
you are asking more of the builder than it can currently handle. Consider
simplifying your request or waiting until we catch up.

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
