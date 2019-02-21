from distutils.core import setup

setup(
    name='apscheduler-dramatiq-executor',
    version='1.0.0',
    packages=['apscheduler_dramatiq_executor'],
    url='https://github.com/cthtuf/apcsheduler-dramatiq-executor',
    license='MIT',
    author='cthtuf',
    author_email='sergey.yarlov@gmail.com',
    description='Executor for APScheduler which doesn\'t execute jobs directrly, but pass it to Dramatiq worker.',
    install_requires=['APScheduler', 'dramatiq[all]'],
)
