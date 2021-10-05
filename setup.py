from setuptools import setup

setup(
    name='asyncweb3',
    version='0.0.1',
    author='TennisBowling',
    author_email='tennisbowling@tennisbowling.com',
    packages=['asyncweb3'],
    url='https://github.com/TennisBowling/asyncweb3',
    license='LICENSE.md',
    description='A python asyncio wrapper for the Ethereum standard API.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    install_requires=[
        'aiohttp',
        'asyncio',
    ],
)
