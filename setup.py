import uuid
from setuptools import setup, find_packages
from pip.req import parse_requirements


def get_requirements(source):
    try:
        install_reqs = parse_requirements(source, session=uuid.uuid1())
    except TypeError:
        # Older version of pip.
        install_reqs = parse_requirements(source)
    required = set([str(ir.req) for ir in install_reqs])
    return required

version = '2.9'

setup(
    name='csnews',
    version=version,
    description="Simple news module",
    long_description=open("README.rst").read(),
    author='Urtzi Odriozola',
    author_email='uodriozola@codesyntax.com',
    url='http://www.codesyntax.com',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications',
    ],
)
