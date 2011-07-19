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

  * mkvitualenv -p python2.7 pythonsg
  * workon pythonsg
  * cd into the root directory of your fork
  * pip install -r requirements.txt
  * cd proj
  * cp local_settings.py.sample local_settings.py
  * mysql -uroot -p
  * create user pythonsg identified by 'pythonsg';
  * create database pythonsg character set utf8 collate utf8_general_ci;
  * grant all on pythonsg.* to pythonsg;
  * exit;
  * python manage.py syncdb --migrate
  * python manage.py collectstatic
  * cd ../proj_media/
  * mkdir media
  * cd media
  * ln -s /path/to/your/venv/lib/python2.7/site-packages/cms/media/cms
  * python manage.py runserver
  