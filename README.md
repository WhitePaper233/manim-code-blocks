# Manim-Code-Blocks

`Manim-Code-Blocks` is a library for [Manim](https://github.com/ManimCommunity/manim) that allows animating blocks of code in Manim videos and scenes. 

## Example Usage

```python
from manim import *
from manim_code_blocks import *


class Main(Scene):

    def construct(self):

        java = CodeBlock(
            """
            public class Main {
                public static void main(String[] args) {
                    System.out.println("Hello world");
                }
            }
            """,
            language = Java
        )

        self.play(*java.create(run_time = 3))
```
Outputs:<br>

![](assets/java_demo.gif)

## Problems & Limitations

### Limited Language Support
Currently only the following languages are supported for syntax highlighting:

- C
- C#
- C++
- Java
- JavaScript
- Lua
- Go
- Python
- Rust
- TypeScript

To add language support, read the new language support guide and submit a pull request.

### Unintelligent Highlighting

The syntax highlighting provided by `Manim-Code-Blocks` is largely trival and can in many cases be inaccurate. The source code is only tokenized, not parsed, and as such accurate token type identification can be impossible for certain circumstances. Syntax highlighting is provided by the [Tokenize-All](https://github.com/NicholasIapalucci/Tokenize-All) module, which is also largely trival and lacks thorough language support. Additionally many languages have not been thoroughly tested enough for accurate coloring. If you find an issue in your syntax highlighting, please report it to [the issues thread](https://github.com/NicholasIapalucci/manim-code-blocks/issues).