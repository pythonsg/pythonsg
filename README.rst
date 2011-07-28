==========
python.sg
==========

This project is a community effort of the local Python community in Singapore.

Contributing
=============

If you want to contribute to this project, you need to follow a few simple 
steps:

  * Fork this repository
  * Create a feature branch
  * Implement your changes
  * Send us a pull request
  
Installation
=============

After forking this project, the following commands should get you a working
local development environment quickly (assuming you use virtualenvwrapper):

  * mkvirtualenv -p python2.7 pythonsg
  * workon pythonsg
  * cd into the root directory of your pythonsg clone
  * pip install --upgrade -r requirements.txt
  * cd proj
  * cp local_settings.py.sample local_settings.py
  * ./manage.py syncdb --migrate
  * ./manage.py collectstatic
  * cd ../proj_public/
  * mkdir media
  * cd media
  * ln -s /path/to/your/venv/lib/python2.7/site-packages/cms/media/cms
  * cd ../../proj/
  * ./manage.py runserver

Loading initial data
=====================

If you want to load your fresh database with some initial testdata, you can use
our fixtures::

  ./manage.py loaddata fixtures/cms.json
  ./manage.py loaddata fixtures/cms.plugins.text.json
  ./manage.py loaddata fixtures/cmsplugin_blog.json
