# saber_test_task 

# ABOUT 
There is project realizing simple data storage and handling it by queries.
Builtin models allows to find dependencies between data objects when initializing.
Data contained in 'yaml' format files defining automatically using selected path in config-file.

# BUILT-IN
- _Python 3.9_;
- Advanced logging: _loguru_;
- Testing: _Python unittest_.

# USAGE
- Start main.py using commandline arguments specifying data-query. For example:
    - _'python main.py list tasks/builds'_ - initiate the showing list of all model objects stored in database;
    - _'python main.py get build/task *object name*'_ - getting object defined by name if exists with its:
        - included list of tasks sorted by tasks and their dependencies (for builds-object);
        - task dependencies (for tasks-object).
