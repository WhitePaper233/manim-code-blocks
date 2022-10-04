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

        self.play(*java.create())
```
Outputs:<br>

![](assets/java_demo.mp4)
