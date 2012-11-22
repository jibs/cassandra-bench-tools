from fabric.api import *
import manage

REMOTE_CONFIG_LOCATION = '/etc/cassandra'
REMOTE_JAR_LOCATION = '/usr/share/cassandra'

LOCAL_JAR_LOCATION = './assets/jna/*.jar'
LOCAL_CONFIG_LOCATION = manage.output_dir

env.hosts = open('hosts', 'r').readlines()
env.user = 'ubuntu'

def push_jars():
    with cd(REMOTE_JAR_LOCATION):
        put(LOCAL_JAR_LOCATION, 'lib', use_sudo=True)

@parallel
def push_configs():
    put(LOCAL_CONFIG_LOCATION + '/*', REMOTE_CONFIG_LOCATION, use_sudo=True)

@parallel
def bounce():
    sudo('service cassandra restart')