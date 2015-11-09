from setuptools import setup, find_packages
setup(
    name = "ImageGrabber",
    version = "0.0.1",
    packages = find_packages(),

    # requirements
    install_requires = [
        'beautifulsoup4==4.4.1',
        'Flask==0.10.1',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'MarkupSafe==0.23',
        'requests==2.8.1',
        'Werkzeug==0.10.4',
        'wheel==0.24.0'
    ],

    author = "Brent Rotz",
    author_email = "rotzbrent@gmail.com",
    description = "Deeplocal challenge",
)
