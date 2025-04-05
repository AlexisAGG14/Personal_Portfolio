"""
Add the About Me view
"""
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon, paragraph_normal_and_bold

# GENERAL VARS
HEADER_TITLE = "About me"


def about_me():
    """About Me view"""
    return rx.center(
        rx.desktop_only(
            __desktop_about_me()
        ),
        rx.mobile_and_tablet(
            __mobile_about_me()
        ),
        id="about_me"
    )


def __desktop_about_me():
    """Desktop view for the About me view"""
    return rx.box(
        section_header_icon(
            "user",
            HEADER_TITLE
        ),
        rx.hstack(
            __info_about_me("75%"),
            # rx.flex(
            #    rx.vstack(
            #        rx.image(
            #            src="/gato.jpeg",
            #            width="auto",
            #            height="250px",
            #            border_radius="30px"
            #        ),
            #        rx.image(
            #            src="/chop.jpeg",
            #            width="auto",
            #            height="250px",
            #            border_radius="30px"
            #        )
            #    ),
            #    width="25%",
            #    justify="center",
            #    align="center"
            # ),
            width="100%",
            margin_top="4em",
            align="center"
        ),
        width="100%",
    )


def __mobile_about_me():
    """Mobile view for the About me view"""
    return rx.box(
        section_header_icon(
            "user",
            HEADER_TITLE
        ),
        rx.vstack(
            # rx.flex(
            #    rx.hstack(
            #        rx.image(
            #            src="/gato.jpeg",
            #            width="auto",
            #            height="200px",
            #            border_radius="30px"
            #        ),
            #        rx.image(
            #            src="/chop.jpeg",
            #            width="auto",
            #            height="200px",
            #            border_radius="30px"
            #        ),
            #    ),
            #    justify="center",
            #    align="center"
            # ),
            __info_about_me(),
            width="100%",
            margin_top="4em",
            align="center",
            spacing="6"
        ),
        width="100%",
    )


def __info_about_me(width: str = "100%"):
    """Return the `About me` information"""
    return rx.vstack(
        paragraph_normal_and_bold(
            "I'm Alexis Gómez, a Mexican, dedicated and skilled ",
            ":bold:Data Analyst",
            " with a strong background in Problem Solving, Analysis,"
            " Looking for insights and Data Science basics.",
            "\n",
        ),
        paragraph_normal_and_bold(
            "I hold a ",
            ":bold:BSc. in Physics",
            ", where I specialized as a"
            " Computational Physicist, with a focus on Materials Science,"
            " where I learned about the behaviour of certain materials under different",
            " conditions, and how to use the tools that the lab had to analyse the data.",
            "\n",
        ),
        paragraph_normal_and_bold(
            "During my Bachelor, I use Python for research purposes,"
            " and learn about the correct",
            " use of the programming as a tool for research,"
            " I worked with molecular dynamics simulations",
            " doing statistics and reporting as a Research Assistant",
            " on the Materials Science department",
            " Earning my first experience in the field of Data Science.",
            "Thing that later",
            " help me to obtain my first job as Software Engineer",
            "at the moment of being gratuated.",
            "That Job, here on ",
            ":bold:Valiot",
            " give me the expertise of how it really feels to work to solve real world problems,",
            " thing that later it would give me the experience to develop my own projects.",
            " and myself in this field.",
        ),
        paragraph_normal_and_bold(
            " I get a lot of love in programming, specially in the kind that help us to understand",
            " How the world works, and how we can use the tools that we have to solve real world problems.",
            " I love history, I love to understand the reality, the scenarios, the conditions, and how this",
            " Leads us to a result or other, understandign the world as it is is the first step to change it",
            " And make it better.",
            " start on Valiot, I firstly start as an Implementor for",
            ":bold: ValueChainOS",
            ", using the",
            " tools that the Product team was developing to improve the implementation process,",
            " but in the first months I noticed my passion for the data understanding,",
            " Thing that lead me to keep working in the software development as data scientist but always with",
            " a passionate view for the analysis of our data and models, and how can we obtain better results.",
            " I love to learn new things, and I am always looking for new challenges.",
        ),
        paragraph_normal_and_bold(
            "That mindset and my passion for new opportunities, gave me the opportunity to work on",
            " in the actual company where I am now,",
            ":bold: Chubb",
            " where I analyze multiple sources of data to mantain metrics repositories, ensuring technical and",
            " business definitions, bringing support to the business team, and also developing new metrics.",
            " Documenting new KPI's, establishing a solid bridge bridge between the business and the data team.",
            " "
        ),
        paragraph_normal_and_bold(
            " I love my parents, my brothers and my niece.",
            " I like to dance and doing excercise, the football, the videogames and reading.",
            " One of my goals for 2025 is to learn ",
            ":bold:Chinese Mandarin",
            " I love learning",
            " and understanding the culture of other countries.",
            " I am a big fan of the idea that ",
            ":bold:you have to give it all, in all your life.",
            " Idea that, with my family and friends helped me to achieve my goals.",
        )
    )
