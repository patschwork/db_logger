from setuptools import setup

setup(
   name='py_db_logger',
   version='1.1',
   description='A log handler to write to different type of databases with a file as fallback solution',
   author='Reza AGHaMohammadi / enhanced by Patrick Schmitz',
   author_email='foomail@foo.example',
   packages=['db_logger'],
   install_requires=['SQLAlchemy'],
)