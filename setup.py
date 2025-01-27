import setuptools

with open('README.md', encoding="utf-8") as f:
    description = f.read()

setuptools.setup(
    name='linux-mouse-record',
    version="2.0",
    author='Read with ai',
    author_email='talwrii@gmail.com',
    long_description_content_type='text/markdown',
    description='Simple CLI to record and replay mouse events',
    install_requires=["pynput"],
    url="https://github.com/talwrii/linux-mouse-record",
    license='MIT',
    keywords='mouse, LINUX, record',
    packages=["linux_mouse_record"],
    long_description=description,
    entry_points={
        'console_scripts': [
            'linux-mouse-record=linux_mouse_record.record:main',
            'linux-mouse-replay=linux_mouse_record.replay:main',
                  ]
    },
    classifiers=[],
)
