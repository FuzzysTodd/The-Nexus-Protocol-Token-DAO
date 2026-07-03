def get_json_content(file_path):
    """
    Load json file content

    Parameters
    ----------
    file_path:
        path to the file

    Raises
    ------
    TypeError
        Error with the file path
    """
def generate_pcs(nni_search_space_content):
    """
    Generate the Parameter Configuration Space (PCS) which defines the
    legal ranges of the parameters to be optimized and their default values.
    Generally, the format is:
    # parameter_name categorical {value_1, ..., value_N} [default value]
    # parameter_name ordinal {value_1, ..., value_N} [default value]
    # parameter_name integer [min_value, max_value] [default value]
    # parameter_name integer [min_value, max_value] [default value] log
    # parameter_name real [min_value, max_value] [default value]
    # parameter_name real [min_value, max_value] [default value] log
    Reference: https://automl.github.io/SMAC3/stable/options.html

    Parameters
    ----------
    nni_search_space_content: search_space
        The search space in this experiment in nni

    Returns
    -------
    Parameter Configuration Space (PCS)
        the legal ranges of the parameters to be optimized and their default values

    Raises
    ------
    RuntimeError
        unsupported type or value error or incorrect search space
    """
def generate_scenario(ss_content):
    """
    Generate the scenario. The scenario-object (smac.scenario.scenario.Scenario) is used to configure SMAC and
    can be constructed either by providing an actual scenario-object, or by specifing the options in a scenario file.
    Reference: https://automl.github.io/SMAC3/stable/options.html
    The format of the scenario file is one option per line:
    OPTION1 = VALUE1
    OPTION2 = VALUE2
    ...
    Parameters
    ----------
    abort_on_first_run_crash: bool
        If true, SMAC will abort if the first run of the target algorithm crashes. Default: True,
        because trials reported to nni tuner would always in success state
    algo: function
        Specifies the target algorithm call that SMAC will optimize. Interpreted as a bash-command.
        Not required by tuner, but required by nni's training service for running trials
    always_race_default:
        Race new incumbents always against default configuration
    cost_for_crash:
        Defines the cost-value for crashed runs on scenarios with quality as run-obj. Default: 2147483647.0.
        Trials reported to nni tuner would always in success state
    cutoff_time:
        Maximum runtime, after which the target algorithm is cancelled. `Required if *run_obj* is runtime`
    deterministic: bool
        If true, the optimization process will be repeatable.
    execdir:
        Specifies the path to the execution-directory. Default: .
        Trials are executed by nni's training service
    feature_file:
        Specifies the file with the instance-features.
        No features specified or feature file is not supported
    initial_incumbent:
        DEFAULT is the default from the PCS. Default: DEFAULT. Must be from: [‘DEFAULT’, ‘RANDOM’].
    input_psmac_dirs:
        For parallel SMAC, multiple output-directories are used.
        Parallelism is supported by nni
    instance_file:
        Specifies the file with the training-instances. Not supported
    intensification_percentage:
        The fraction of time to be used on intensification (versus choice of next Configurations). Default: 0.5.
        Not supported, trials are controlled by nni's training service and kill be assessor
    maxR: int
        Maximum number of calls per configuration. Default: 2000.
    memory_limit:
        Maximum available memory the target algorithm can occupy before being cancelled.
    minR: int
        Minimum number of calls per configuration. Default: 1.
    output_dir:
        Specifies the output-directory for all emerging files, such as logging and results.
        Default: smac3-output_2018-01-22_15:05:56_807070.
    overall_obj:
    \tPARX, where X is an integer defining the penalty imposed on timeouts (i.e. runtimes that exceed the cutoff-time).
        Timeout is not supported
    paramfile:
        Specifies the path to the PCS-file.
    run_obj:
        Defines what metric to optimize. When optimizing runtime, cutoff_time is required as well.
        Must be from: [‘runtime’, ‘quality’].
    runcount_limit: int
        Maximum number of algorithm-calls during optimization. Default: inf.
        Use default because this is controlled by nni
    shared_model:
        Whether to run SMAC in parallel mode. Parallelism is supported by nni
    test_instance_file:
        Specifies the file with the test-instances. Instance is not supported
    tuner-timeout:
        Maximum amount of CPU-time used for optimization. Not supported
    wallclock_limit: int
        Maximum amount of wallclock-time used for optimization. Default: inf.
        Use default because this is controlled by nni

    Returns
    -------
    Scenario:
        The scenario-object (smac.scenario.scenario.Scenario) is used to configure SMAC and can be constructed
        either by providing an actual scenario-object, or by specifing the options in a scenario file
    """
