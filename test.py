from src.manim_code_blocks import *
from manim import *


class Main(Scene):

    def construct(self):

        java = CodeBlock(
            """
            public class Main {
                public static void main(String[] args) {
                    System.out.println("Hello world");
                }
            }}
            """,
            language = Java
        )

        self.play(*java.create())