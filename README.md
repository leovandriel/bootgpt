# BootGPT

*Write code using almost only prompts and GPT.*

## Usage

Put your OpenAI API key in a file called `key.txt`:

    chmod 600 key.txt

Boot it:

    python -m boot

## About

Let's build an application for software engineering with prompts, using only
prompts.

## Booting

`boot.py` is the only Python source file in this project. It forms the start of
a bootstrap sequence that sets up an increasingly capable programming toolchain.
`boot.py` is intentionally minimal.

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

*Why not just write one big prompt that builds the whole application in one go?*

That would be great. Primary reason is that the OpenAI API does not write files
or create projects, it just returns text, so we still need to write code to
transform this text into a folder structure. The whole point of this project is
not to write code, but to use prompts, so we're left with bootstrapping from
much shorter and detailed prompts. Also, I haven't managed to get GPT to write
large amounts of functioning code from a single prompt.

## License

MIT
