import logging
import subprocess
import traceback

from ..schemas.mutations import ProcessResult

__all__ = [
    'launch_workstations',
]

LOG = logging.getLogger(__name__)


def launch_workstations(image_id, user, ip_address):
    """
    :param str image_id:
    :param str user:
    :param str ip_address:
    """
    LOG.debug('launch workstation...')
    try:
        process = subprocess.Popen(
            ['kubectl', '...'],  # TODO: Replace this with the real command
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        std_out, std_err = process.communicate()

        return ProcessResult(
            exit_code=process.returncode,
            response=std_err or std_out
        )

    except Exception as ex:
        LOG.error(traceback.format_exc())
        return ProcessResult(
            exit_code=-1,
            response=str(ex)
        )
