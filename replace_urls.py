"""
File in Python that include a function that replace all the URLs by a pre-determined url
"""
import os
import re

patterns = [
    r'/gato.jpeg', r'/profile_pic.jpg',
    r'/favicon.ico', r'/_next/static/',
    r'/projects', r'https://www.credly.com/',
    r'https://coursera.org/'
]


def replace_patterns(url: str) -> None:
    """Replace relative URLs with absolute URLs in the index.html file.

    This function is crucial for making external links work correctly in the deployed
    application. It processes URLs for static assets and external links, including
    certificate URLs. Without proper URL replacement, buttons like "See certificate"
    might not function correctly.

    Args:
        url (str): The base URL to prepend to all relative paths. For example,
                  'https://yourdomain.com' or the deployment URL.

    Example:
        If url = 'https://portfolio.com' and a certificate link is '/projects/cert.pdf',
        it becomes 'https://portfolio.com/projects/cert.pdf'
    """
    # Read the index.html file
    with open('./index.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Modificar el contenido del archivo HTML
    for pattern in patterns:
        content = re.sub(pattern, f'{url}{pattern}', content)

    # Guardar el contenido modificado en un nuevo archivo HTML
    with open('./index.html', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    replace_patterns(
        os.environ.get("URL", "")
    )
