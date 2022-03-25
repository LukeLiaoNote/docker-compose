import os
import subprocess
import yaml
import docker
import sys
import argparse


current_dir = os.getcwd()
def get_services():
    current_dir = os.getcwd()

    # services = [x if 'docker-compose.yml' in [ y if os.path.isdir(os.path.join(current_dir, y))  in os.listdir(current_dir)]]

    services = [d for d in os.listdir(current_dir) if os.path.isdir(d) and os.path.exists(os.path.join(current_dir,d + '/docker-compose.yml' ))]
    return services

# print(get_services())

def get_container_status(container_name):
    client = docker.DockerClient(base_url='unix://var/run/docker.sock',version='auto',timeout=10)
    container_status = 'stoped'
    docker_list = client.containers.list()
    for i in range(len(docker_list)):
        docker_name = client.containers.list()[i].name
        if container_name in docker_name:
            container_id = client.containers.list()[i].id[:10]
            container_status = client.containers.get(container_id).status
    return container_status


def get_compose_data(yml_file):
    contaners = []

    s_path = os.path.split(os.path.dirname(os.path.abspath(yml_file)))[1]
    with open(yml_file, 'r', encoding='utf-8') as f:
        content = yaml.load(f.read(),Loader=yaml.FullLoader)
        for service in content['services']:
            service_name = content['services'][service].get('container_name', s_path + '_' +  service + '_1')
            image = content['services'][service]['image']
            status = get_container_status(service_name)
            contaners.append({"container_name": service_name, "image": image, "status": status})

            # container_name = service.get('container_name', s_path + '_' + )
        # return yaml.load(content)
    return contaners

def start(service):
    workspace = os.path.join(current_dir,service)
    subprocess.run('/usr/local/bin/docker-compose up -d',shell=True,cwd=workspace)

def stop(service):
    workspace = os.path.join(current_dir,service)
    subprocess.run('/usr/local/bin/docker-compose down',shell=True,cwd=workspace)

def restart(service):
    stop(service)
    start(service)

def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("service",help = "the service to be managed.",action = "store")
    parser.add_argument("-s", "--start", help = "start the service(s)",action = "store_true" )
    parser.add_argument("-p", "--stop", help = "stop the service(s).",action = "store_true")
    parser.add_argument("-r", "--restart", help = "restart the service(s).",action = "store_true")
    args = parser.parse_args()
    global start,stop,restart
    service = args.service
    option = start if args.start else restart if args.restart else stop
    option(service)

for s in get_services():
    print('*' * 40 , 'Loading {}'.format(s), '*' * 40)
    print(get_compose_data(os.path.join(os.path.join(current_dir, s), 'docker-compose.yml')))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("service",help = "the service to be managed.",action = "store")
    parser.add_argument("-s", "--start", help = "start the service(s)",action = "store_true" )
    parser.add_argument("-p", "--stop", help = "stop the service(s).",action = "store_true")
    parser.add_argument("-r", "--restart", help = "restart the service(s).",action = "store_true")
    args = parser.parse_args()
    service = args.service
    if args.start:
        start(service)
    if args.stop:
        stop(servcie)
    if args.restart:
        restart(service)

