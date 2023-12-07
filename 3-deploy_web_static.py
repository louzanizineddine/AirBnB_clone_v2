#!/usr/bin/python3
from fabric.api import local, task, run, put, env
from datetime import datetime
import os

env.hosts = ["100.25.22.28", "100.26.226.197"]
env.user = 'ubuntu'


@task
def do_pack():
    """genereate archive from web_static folder to deploy static web"""

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + date + '.tgz'
    if not (os.path.exists("versions")):
        local('mkdir -p versions')
    local('tar -cvzf ' + path + ' web_static')
    if (os.path.exists(path)):
        return path
    return None


@task
def do_deploy(archive_path):
    """deploy static archive to the servers web to servers"""

    if not (os.path.exists(archive_path)):
        return False

    try:
        put(archive_path, "/tmp/")
        fileName = archive_path.split('/')[-1]
        fileNameWithNoExtension = fileName.split('.')[0]
        path = '/data/web_static/releases/' + fileNameWithNoExtension
        run('mkdir -p ' + path)
        run('tar -xzf /tmp/' + fileName + ' -C ' + path)
        run('rm /tmp/' + fileName)
        run('mv ' + path + '/web_static/* ' + path)
        run('rm -rf ' + path + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s ' + path + ' /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False


@task
def deploy():
    """resume all tasks to deploy static web"""
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
