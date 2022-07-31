import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
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
