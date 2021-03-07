from setuptools import setup, find_packages


setup(
    name="serenity",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'flask',
        'graphene',
        'neo4j',
        'flask-graphql',
    ],
)
