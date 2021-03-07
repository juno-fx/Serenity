import logging
import subprocess
import traceback

from ..schemas.mutations import ProcessResult

__all__ = [
    'launch_workstations',
]

LOG = logging.getLogger(__name__)


def launch_workstations(image_id: str, user: str) -> 'ProcessResult':
    """
    Launch a workstation

    :param image_id: the image id to load on this workstation
    :param user: the user to assign to this workstation
    """
    # pylint: disable=broad-except
    LOG.debug('launch workstation...')
    try:
        process = subprocess.Popen(
            ['kubectl', '...', image_id, '...', user],  # TODO: Replace this with the real command
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
