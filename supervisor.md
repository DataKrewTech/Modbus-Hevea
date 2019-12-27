### Script Exceptions
An exception in the long running python script can stop it and stop
the telemetery data. Most of the exceptions can be handled using 
exception handling, however some unknown exceptions can create issues.

### Supervised Scripts
The scripts need to be run under a supervisor process which can monitor
the script status. In case the script stops, the supervisor logs the 
reason for the exception and restarts the script.

### Steps to Add Supervision

- Install supervisor package
  `sudo apt-get install -y supervisor`
- Start supervisor service
  `sudo service supervisor start`
- Add configuration script
  All the supervised scripts need to be added at the path `/etc/supervisor/conf.d/`
  An example configuration script can be seen in the file `./python_script.conf`.
- Add folder for log files.
  - The stdout and stderror log files for the script can be placed at `/var/log/{your folder}/`,
    this directory needs to be created as supervisor will not handle the creation.
- The status of the the running script can be seen with the command
  `sudo supervisorctl`
