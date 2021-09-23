Install the latest
===================

To install the latest version of neuroio simply run:

`pip3 install neuroio`

OR

`poetry add neuroio`

OR

`pipenv install neuroio`


Changelog
=========
* 0.0.7
    * Updated library to latest API version (at the time of this release - 1.3.0)
    * Updated requirements
    * Updated README & docs
* 0.0.6
    * Updated library to latest API version (at the time of this release - 1.2.1)
    * Updated README & docs
* 0.0.5
    * Fixed persistent connection problems
    * Updated requirements
    * Codebase cleanup
* 0.0.4
    * Changed the way how we treat httpx connection - now we don't close it after every request (which was supposedly right way in httpx docs)
* 0.0.3
    * Updated httpx version, disabled cruft check since it just messes up project files