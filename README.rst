===========
Description
===========
This package simple as hell. It provides one class which could be used as APScheduler executor.

It could be useful if you're using either APscheduler and Dramatiq and want to keep APscheduler as lightweight worker which only schedule tasks and Dramatiq as scalable task executor.

Note:  Tasks could be executed not in the same time as in Job.run_next_time because of high load of the Dramatiq worker or any latencies in broker.

=============
How to use it
=============

***************
Install
***************
Install package via pip::

  pip install apscheduler-dramatiq-executor

***************
Configure
***************
Put executor in apscheduler config::

  APSCHEDULER_SETTINGS = {
    ...
    'apscheduler.executors.default': {
      'class': 'apscheduler_dramatiq_executor.executor:DramatiqExecutor',
    },  
  }

