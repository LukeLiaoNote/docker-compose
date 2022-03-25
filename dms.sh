#!/bin/bash

###########################################
#   
#  统一管理middleware容器入口
# 
#  Internal only ， contact IT team for help
#
###########################################

CURRENT_PATH=$(pwd)
# 获取当前目录下所有包含docker-compose.yml的文件夹，文件夹名字作为service name
function list_all_midwares() {

    for m in `ls -d */`; do
        # echo "${m}docker-compose.yml"
    
        if [ -e "${m}docker-compose.yml" ];
        then 
            status_service ${m} | grep -v "Command" | grep -v "^---"

        fi
        
    done

}

function up_service(){
    echo "[ ${1} ] Starting... "
    cd ${1} && docker-compose up -d
    [[ $? -eq 0 ]] && echo "[ ${1} ] Started successfully !" || "[ ${1} ] Started failed !\n RUN: \n cd ${1} ; docker-compose logs ${1} \n  to check logs"
}

function status_service(){
    cd ${1} && docker-compose ps
}

function stop_service(){
    echo "[ ${1} ]Stopping ..."
    cd ${1} && docker-compose down
}

function restart_service(){
    stop_service ${1}
    start_service ${1}
}

function usage(){
    echo
    echo "This is a management script for quickly running middlewares, managed by ops team ."
    echo "git repo : https://gitlab.derinow.io/ops/docker-middleware.git"
    echo
    echo
    echo "$0 [ start | stop | restart | list ] service_name"
    echo "      start   -  up containers defined in specified directory, eg $0 start mysql"
    echo "      stop    -  down containers defined in specified directory, eg $0 start mysql"
    echo "      restart -  recreate containers defined in specified directory, eg $0 restart mysql"
    echo "      list    -  list all created services, usage: $0 list"
    exit 128
}
function main(){
    action=${1}

    if [ -n "${2}" ];
    then 
        echo "found 2 is ${2}"
        [[ -f "${2}/docker-compose.yml" ]] && service=${2} || usage
    else

        [ "${action}" = "list" ] || usage
    fi
    case ${action} in
    "start")
    up_service ${service}
    ;;
    "stop")
    stop_service ${service}
    ;;
    "restart")
    restart_service ${service}
    ;;
    "status")
    status_service ${service}
    ;;
    "list")
    list_all_midwares
    ;;
    *)
    usage
    ;;
    esac

}



main $1 $2

