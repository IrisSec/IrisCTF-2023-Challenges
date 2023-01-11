# babyseek - 167 points - 86 solves
I'll let you seek around my file as far as you want, but you can't go anywhere since it's /dev/null.

&nbsp;

To figure out where things are, you can use the `gdb` debugger. I recommend using a Docker instance, such as with the Dockerfile provided, to ensure you have an environment that matches the remote server you are attacking.

[Hint! You can find the location of functions in the Global Offset Table by using their name followed by `@got.plt` - for example, `print &'fwrite@got.plt'`.]

By: sera
