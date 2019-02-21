import sys

from apscheduler.executors.base import BaseExecutor
from dramatiq.broker import get_broker


class DramatiqExecutor(BaseExecutor):
    """
    Executor for APScheduler. Don't run tasks directly, but enque it for running by dramatiq worker
    """
    def _do_submit_job(self, job, run_times):
        try:
            get_broker().get_actor(job.func.actor_name).send(*job.args, **job.kwargs)
        except BaseException:
            self._run_job_error(job.id, *sys.exc_info()[1:])
        else:
            self._run_job_success(job.id, events=[])
