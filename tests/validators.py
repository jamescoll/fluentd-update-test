import time
import os
import re
import requests
import platform
import yaml
import subprocess

from utils import (
    get_arch,
    kubectl,
    wait_for_pod_state,
    kubectl_get,
    wait_for_installation,
    docker,
    update_yaml_with_arch,
    run_until_success,
)

def validate_fluentd():
    """
    Validate fluentd
    """
    if platform.machine() != "x86_64":
        print("Fluentd tests are only relevant in x86 architectures")
        return

    wait_for_pod_state("elasticsearch-logging-0", "kube-system", "running")
    wait_for_pod_state("", "kube-system", "running", label="k8s-app=fluentd-es")
    wait_for_pod_state("", "kube-system", "running", label="k8s-app=kibana-logging")
