#!/usr/bin/python3
"""
genereate archive from web_static folder to deploy static web
"""
from fabric.api import local
from datetime import datetime
import os.path

@task
def do_pack():
    """
    genereate archive from web_static folder to deploy static web
    """

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + date + '.tgz'
    if not (os.path.exists("versions")):
        local('mkdir -p versions')
    local('tar -cvzf ' + path + ' web_static')
    if (os.path.exists(path)):
        return path
    return None