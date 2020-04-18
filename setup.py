from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='bitbucket2github',
    version='1.0',
    description='Simple tool to migrate your Bitbucket repositories to GitHub',
    long_description=readme(),
    url='https://github.com/brunogfranca/bitbucket2github',
    author='Bruno França',
    author_email='bgfranca@gmail.com',
    license='MIT',
    packages=['bitbucket2github'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['bitbucket2github=bitbucket2github.cli:migrate'],
    }
)
