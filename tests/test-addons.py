import pytest
import os
import platform
import sh
import yaml

from validators import (
    validate_fluentd
)
from utils import (
    microk8s_enable,
    wait_for_pod_state,
    wait_for_namespace_termination,
    microk8s_disable,
    microk8s_reset,
    is_container,
)
from subprocess import PIPE, STDOUT, CalledProcessError, check_call, run, check_output


class TestAddons(object):
    @pytest.fixture(scope="session", autouse=True)
    def clean_up(self):
        """
        Clean up after a test
        """
        yield
        microk8s_reset()

def test_fluentd(self):
        """
        Test jaeger, prometheus and fluentd.

        """
        print("Enabling fluentd")
        microk8s_enable("fluentd")
        print("ValidatingFluentd")
        validate_fluentd()
        print("Disabling fluentd")
        microk8s_disable("fluentd")

    @pytest.mark.skipif(
        os.environ.get("STRICT") == "yes",
        reason="Skipping cilium tests in strict confinement as they are expected to fail",
    )
    #@pytest.mark.skipif(
    #    platform.machine() != "x86_64",
    #    reason="Cilium tests are only relevant in x86 architectures",*/
    )
