#Just a notepad

# Introduction #
This page intends to serve as as notepad for memos and others, specially TODO (not exactly issues).


# Notes #

**_Server\_Passive\_Checks.py_**

This artifact is from interface module. However, it is acting like an integration artifact, to whom vms send monitoring info. This behavior must be changed, i.e, vms must sent monitoring data to another service. Server\_Passive\_Checks should just update nagios info, in the interface layer. If it is not running, for instance, all monitoring data from vms are being drop, since the vm monitoring plugin tries to connect in this service.

**_LOGS_**

We need to improve log records, since many problems seems to occur, specially related to service dying. For now I have removed de filemode=w from logging as well as put the server.serve\_forever between a try .. catch statement (and recording the exceptions).