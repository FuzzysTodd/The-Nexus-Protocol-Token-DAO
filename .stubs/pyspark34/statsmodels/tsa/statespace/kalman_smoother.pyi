from _typeshed import Incomplete
from statsmodels.tsa.statespace import initialization as initialization, tools as tools
from statsmodels.tsa.statespace.kalman_filter import FilterResults as FilterResults, KalmanFilter as KalmanFilter
from statsmodels.tsa.statespace.representation import OptionWrapper as OptionWrapper
from statsmodels.tsa.statespace.tools import copy_index_matrix as copy_index_matrix, reorder_missing_matrix as reorder_missing_matrix, reorder_missing_vector as reorder_missing_vector

SMOOTHER_STATE: int
SMOOTHER_STATE_COV: int
SMOOTHER_DISTURBANCE: int
SMOOTHER_DISTURBANCE_COV: int
SMOOTHER_STATE_AUTOCOV: int
SMOOTHER_ALL: Incomplete
SMOOTH_CONVENTIONAL: int
SMOOTH_CLASSICAL: int
SMOOTH_ALTERNATIVE: int
SMOOTH_UNIVARIATE: int

class KalmanSmoother(KalmanFilter):
    """
    State space representation of a time series process, with Kalman filter
    and smoother.

    Parameters
    ----------
    k_endog : {array_like, int}
        The observed time-series process :math:`y` if array like or the
        number of variables in the process if an integer.
    k_states : int
        The dimension of the unobserved state process.
    k_posdef : int, optional
        The dimension of a guaranteed positive definite covariance matrix
        describing the shocks in the measurement equation. Must be less than
        or equal to `k_states`. Default is `k_states`.
    results_class : class, optional
        Default results class to use to save filtering output. Default is
        `SmootherResults`. If specified, class must extend from
        `SmootherResults`.
    **kwargs
        Keyword arguments may be used to provide default values for state space
        matrices, for Kalman filtering options, or for Kalman smoothing
        options. See `Representation` for more details.
    """
    smoother_outputs: Incomplete
    smoother_state: Incomplete
    smoother_state_cov: Incomplete
    smoother_disturbance: Incomplete
    smoother_disturbance_cov: Incomplete
    smoother_state_autocov: Incomplete
    smoother_all: Incomplete
    smooth_methods: Incomplete
    smooth_conventional: Incomplete
    smooth_alternative: Incomplete
    smooth_classical: Incomplete
    smooth_univariate: Incomplete
    smoother_output = SMOOTHER_ALL
    smooth_method: int
    prefix_kalman_smoother_map: Incomplete
    def __init__(self, k_endog, k_states, k_posdef: Incomplete | None = None, results_class: Incomplete | None = None, kalman_smoother_classes: Incomplete | None = None, **kwargs) -> None: ...
    def set_smoother_output(self, smoother_output: Incomplete | None = None, **kwargs) -> None:
        """
        Set the smoother output

        The smoother can produce several types of results. The smoother output
        variable controls which are calculated and returned.

        Parameters
        ----------
        smoother_output : int, optional
            Bitmask value to set the smoother output to. See notes for details.
        **kwargs
            Keyword arguments may be used to influence the smoother output by
            setting individual boolean flags. See notes for details.

        Notes
        -----
        The smoother output is defined by a collection of boolean flags, and
        is internally stored as a bitmask. The methods available are:

        SMOOTHER_STATE = 0x01
            Calculate and return the smoothed states.
        SMOOTHER_STATE_COV = 0x02
            Calculate and return the smoothed state covariance matrices.
        SMOOTHER_STATE_AUTOCOV = 0x10
            Calculate and return the smoothed state lag-one autocovariance
            matrices.
        SMOOTHER_DISTURBANCE = 0x04
            Calculate and return the smoothed state and observation
            disturbances.
        SMOOTHER_DISTURBANCE_COV = 0x08
            Calculate and return the covariance matrices for the smoothed state
            and observation disturbances.
        SMOOTHER_ALL
            Calculate and return all results.

        If the bitmask is set directly via the `smoother_output` argument, then
        the full method must be provided.

        If keyword arguments are used to set individual boolean flags, then
        the lowercase of the method must be used as an argument name, and the
        value is the desired value of the boolean flag (True or False).

        Note that the smoother output may also be specified by directly
        modifying the class attributes which are defined similarly to the
        keyword arguments.

        The default smoother output is SMOOTHER_ALL.

        If performance is a concern, only those results which are needed should
        be specified as any results that are not specified will not be
        calculated. For example, if the smoother output is set to only include
        SMOOTHER_STATE, the smoother operates much more quickly than if all
        output is required.

        Examples
        --------
        >>> import statsmodels.tsa.statespace.kalman_smoother as ks
        >>> mod = ks.KalmanSmoother(1,1)
        >>> mod.smoother_output
        15
        >>> mod.set_smoother_output(smoother_output=0)
        >>> mod.smoother_state = True
        >>> mod.smoother_output
        1
        >>> mod.smoother_state
        True
        """
    def set_smooth_method(self, smooth_method: Incomplete | None = None, **kwargs) -> None:
        """
        Set the smoothing method

        The smoothing method can be used to override the Kalman smoother
        approach used. By default, the Kalman smoother used depends on the
        Kalman filter method.

        Parameters
        ----------
        smooth_method : int, optional
            Bitmask value to set the filter method to. See notes for details.
        **kwargs
            Keyword arguments may be used to influence the filter method by
            setting individual boolean flags. See notes for details.

        Notes
        -----
        The smoothing method is defined by a collection of boolean flags, and
        is internally stored as a bitmask. The methods available are:

        SMOOTH_CONVENTIONAL = 0x01
            Default Kalman smoother, as presented in Durbin and Koopman, 2012
            chapter 4.
        SMOOTH_CLASSICAL = 0x02
            Classical Kalman smoother, as presented in Anderson and Moore, 1979
            or Durbin and Koopman, 2012 chapter 4.6.1.
        SMOOTH_ALTERNATIVE = 0x04
            Modified Bryson-Frazier Kalman smoother method; this is identical
            to the conventional method of Durbin and Koopman, 2012, except that
            an additional intermediate step is included.
        SMOOTH_UNIVARIATE = 0x08
            Univariate Kalman smoother, as presented in Durbin and Koopman,
            2012 chapter 6, except with modified Bryson-Frazier timing.

        Practically speaking, these methods should all produce the same output
        but different computational implications, numerical stability
        implications, or internal timing assumptions.

        Note that only the first method is available if using a Scipy version
        older than 0.16.

        If the bitmask is set directly via the `smooth_method` argument, then
        the full method must be provided.

        If keyword arguments are used to set individual boolean flags, then
        the lowercase of the method must be used as an argument name, and the
        value is the desired value of the boolean flag (True or False).

        Note that the filter method may also be specified by directly modifying
        the class attributes which are defined similarly to the keyword
        arguments.

        The default filtering method is SMOOTH_CONVENTIONAL.

        Examples
        --------
        >>> mod = sm.tsa.statespace.SARIMAX(range(10))
        >>> mod.smooth_method
        1
        >>> mod.filter_conventional
        True
        >>> mod.filter_univariate = True
        >>> mod.smooth_method
        17
        >>> mod.set_smooth_method(filter_univariate=False,
                                  filter_collapsed=True)
        >>> mod.smooth_method
        33
        >>> mod.set_smooth_method(smooth_method=1)
        >>> mod.filter_conventional
        True
        >>> mod.filter_univariate
        False
        >>> mod.filter_collapsed
        False
        >>> mod.filter_univariate = True
        >>> mod.smooth_method
        17
        """
    def smooth(self, smoother_output: Incomplete | None = None, smooth_method: Incomplete | None = None, results: Incomplete | None = None, run_filter: bool = True, prefix: Incomplete | None = None, complex_step: bool = False, update_representation: bool = True, update_filter: bool = True, update_smoother: bool = True, **kwargs):
        """
        Apply the Kalman smoother to the statespace model.

        Parameters
        ----------
        smoother_output : int, optional
            Determines which Kalman smoother output calculate. Default is all
            (including state, disturbances, and all covariances).
        results : class or object, optional
            If a class, then that class is instantiated and returned with the
            result of both filtering and smoothing.
            If an object, then that object is updated with the smoothing data.
            If None, then a SmootherResults object is returned with both
            filtering and smoothing results.
        run_filter : bool, optional
            Whether or not to run the Kalman filter prior to smoothing. Default
            is True.
        prefix : str
            The prefix of the datatype. Usually only used internally.

        Returns
        -------
        SmootherResults object
        """

class SmootherResults(FilterResults):
    """
    Results from applying the Kalman smoother and/or filter to a state space
    model.

    Parameters
    ----------
    model : Representation
        A Statespace representation

    Attributes
    ----------
    nobs : int
        Number of observations.
    k_endog : int
        The dimension of the observation series.
    k_states : int
        The dimension of the unobserved state process.
    k_posdef : int
        The dimension of a guaranteed positive definite covariance matrix
        describing the shocks in the measurement equation.
    dtype : dtype
        Datatype of representation matrices
    prefix : str
        BLAS prefix of representation matrices
    shapes : dictionary of name:tuple
        A dictionary recording the shapes of each of the representation
        matrices as tuples.
    endog : ndarray
        The observation vector.
    design : ndarray
        The design matrix, :math:`Z`.
    obs_intercept : ndarray
        The intercept for the observation equation, :math:`d`.
    obs_cov : ndarray
        The covariance matrix for the observation equation :math:`H`.
    transition : ndarray
        The transition matrix, :math:`T`.
    state_intercept : ndarray
        The intercept for the transition equation, :math:`c`.
    selection : ndarray
        The selection matrix, :math:`R`.
    state_cov : ndarray
        The covariance matrix for the state equation :math:`Q`.
    missing : array of bool
        An array of the same size as `endog`, filled with boolean values that
        are True if the corresponding entry in `endog` is NaN and False
        otherwise.
    nmissing : array of int
        An array of size `nobs`, where the ith entry is the number (between 0
        and k_endog) of NaNs in the ith row of the `endog` array.
    time_invariant : bool
        Whether or not the representation matrices are time-invariant
    initialization : str
        Kalman filter initialization method.
    initial_state : array_like
        The state vector used to initialize the Kalamn filter.
    initial_state_cov : array_like
        The state covariance matrix used to initialize the Kalamn filter.
    filter_method : int
        Bitmask representing the Kalman filtering method
    inversion_method : int
        Bitmask representing the method used to invert the forecast error
        covariance matrix.
    stability_method : int
        Bitmask representing the methods used to promote numerical stability in
        the Kalman filter recursions.
    conserve_memory : int
        Bitmask representing the selected memory conservation method.
    tolerance : float
        The tolerance at which the Kalman filter determines convergence to
        steady-state.
    loglikelihood_burn : int
        The number of initial periods during which the loglikelihood is not
        recorded.
    converged : bool
        Whether or not the Kalman filter converged.
    period_converged : int
        The time period in which the Kalman filter converged.
    filtered_state : ndarray
        The filtered state vector at each time period.
    filtered_state_cov : ndarray
        The filtered state covariance matrix at each time period.
    predicted_state : ndarray
        The predicted state vector at each time period.
    predicted_state_cov : ndarray
        The predicted state covariance matrix at each time period.
    kalman_gain : ndarray
        The Kalman gain at each time period.
    forecasts : ndarray
        The one-step-ahead forecasts of observations at each time period.
    forecasts_error : ndarray
        The forecast errors at each time period.
    forecasts_error_cov : ndarray
        The forecast error covariance matrices at each time period.
    loglikelihood : ndarray
        The loglikelihood values at each time period.
    collapsed_forecasts : ndarray
        If filtering using collapsed observations, stores the one-step-ahead
        forecasts of collapsed observations at each time period.
    collapsed_forecasts_error : ndarray
        If filtering using collapsed observations, stores the one-step-ahead
        forecast errors of collapsed observations at each time period.
    collapsed_forecasts_error_cov : ndarray
        If filtering using collapsed observations, stores the one-step-ahead
        forecast error covariance matrices of collapsed observations at each
        time period.
    standardized_forecast_error : ndarray
        The standardized forecast errors
    smoother_output : int
        Bitmask representing the generated Kalman smoothing output
    scaled_smoothed_estimator : ndarray
        The scaled smoothed estimator at each time period.
    scaled_smoothed_estimator_cov : ndarray
        The scaled smoothed estimator covariance matrices at each time period.
    smoothing_error : ndarray
        The smoothing error covariance matrices at each time period.
    smoothed_state : ndarray
        The smoothed state at each time period.
    smoothed_state_cov : ndarray
        The smoothed state covariance matrices at each time period.
    smoothed_state_autocov : ndarray
        The smoothed state lago-one autocovariance matrices at each time
        period: :math:`Cov(\\alpha_{t+1}, \\alpha_t)`.
    smoothed_measurement_disturbance : ndarray
        The smoothed measurement at each time period.
    smoothed_state_disturbance : ndarray
        The smoothed state at each time period.
    smoothed_measurement_disturbance_cov : ndarray
        The smoothed measurement disturbance covariance matrices at each time
        period.
    smoothed_state_disturbance_cov : ndarray
        The smoothed state disturbance covariance matrices at each time period.
    """
    def update_representation(self, model, only_options: bool = False) -> None:
        """
        Update the results to match a given model

        Parameters
        ----------
        model : Representation
            The model object from which to take the updated values.
        only_options : bool, optional
            If set to true, only the smoother and filter options are updated,
            and the state space representation is not updated. Default is
            False.

        Notes
        -----
        This method is rarely required except for internal usage.
        """
    innovations_transition: Incomplete
    scaled_smoothed_diffuse_estimator: Incomplete
    scaled_smoothed_diffuse1_estimator_cov: Incomplete
    scaled_smoothed_diffuse2_estimator_cov: Incomplete
    scaled_smoothed_estimator_presample: Incomplete
    scaled_smoothed_estimator: Incomplete
    scaled_smoothed_estimator_cov_presample: Incomplete
    scaled_smoothed_estimator_cov: Incomplete
    def update_smoother(self, smoother) -> None:
        """
        Update the smoother results

        Parameters
        ----------
        smoother : KalmanSmoother
            The model object from which to take the updated values.

        Notes
        -----
        This method is rarely required except for internal usage.
        """
    def smoothed_state_autocovariance(self, lag: int = 1, t: Incomplete | None = None, start: Incomplete | None = None, end: Incomplete | None = None, extend_kwargs: Incomplete | None = None):
        '''
        Compute state vector autocovariances, conditional on the full dataset

        Computes:

        .. math::

            Cov(\\alpha_t - \\hat \\alpha_t, \\alpha_{t - j} - \\hat \\alpha_{t - j})

        where the `lag` argument gives the value for :math:`j`. Thus when
        the `lag` argument is positive, the autocovariance is between the
        current and previous periods, while if `lag` is negative the
        autocovariance is between the current and future periods.

        Parameters
        ----------
        lag : int, optional
            The number of period to shift when computing the autocovariance.
            Default is 1.
        t : int, optional
            A specific period for which to compute and return the
            autocovariance. Cannot be used in combination with `start` or
            `end`. See the Returns section for details on how this
            parameter affects what is what is returned.
        start : int, optional
            The start of the interval (inclusive) of autocovariances to compute
            and return. Cannot be used in combination with the `t` argument.
            See the Returns section for details on how this parameter affects
            what is what is returned. Default is 0.
        end : int, optional
            The end of the interval (exclusive) autocovariances to compute and
            return. Note that since it is an exclusive endpoint, the returned
            autocovariances do not include the value at this index. Cannot be
            used in combination with the `t` argument. See the Returns section
            for details on how this parameter affects what is what is returned
            and what the default value is.
        extend_kwargs : dict, optional
            Keyword arguments containing updated state space system matrices
            for handling out-of-sample autocovariance computations in
            time-varying state space models.

        Returns
        -------
        acov : ndarray
            Array of autocovariance matrices. If the argument `t` is not
            provided, then it is shaped `(k_states, k_states, n)`, while if `t`
            given then the third axis is dropped and the array is shaped
            `(k_states, k_states)`.

            The output under the default case differs somewhat based on the
            state space model and the sign of the lag. To see how these cases
            differ, denote the output at each time point as Cov(t, t-j). Then:

            - If `lag > 0` (and the model is either time-varying or
              time-invariant), then the returned array is shaped `(*, *, nobs)`
              and each entry [:, :, t] contains Cov(t, t-j). However, the model
              does not have enough information to compute autocovariances in
              the pre-sample period, so that we cannot compute Cov(1, 1-lag),
              Cov(2, 2-lag), ..., Cov(lag, 0). Thus the first `lag` entries
              have all values set to NaN.

            - If the model is time-invariant and `lag < -1` or if `lag` is
              0 or -1, and the model is either time-invariant or time-varying,
              then the returned array is shaped `(*, *, nobs)` and each
              entry [:, :, t] contains Cov(t, t+j). Moreover, all entries are
              available (i.e. there are no NaNs).

            - If the model is time-varying and `lag < -1` and `extend_kwargs`
              is not provided, then the returned array is shaped
              `(*, *, nobs - lag + 1)`.

            - However, if the model is time-varying and `lag < -1`, then
              `extend_kwargs` can be provided with `lag - 1` additional
              matrices so that the returned array is shaped `(*, *, nobs)` as
              usual.

            More generally, the dimension of the last axis will be
            `start - end`.

        Notes
        -----
        This method computes:

        .. math::

            Cov(\\alpha_t - \\hat \\alpha_t, \\alpha_{t - j} - \\hat \\alpha_{t - j})

        where the `lag` argument determines the autocovariance order :math:`j`,
        and `lag` is an integer (positive, zero, or negative). This method
        cannot compute values associated with time points prior to the sample,
        and so it returns a matrix of NaN values for these time points.
        For example, if `start=0` and `lag=2`, then assuming the output is
        assigned to the variable `acov`, we will have `acov[..., 0]` and
        `acov[..., 1]` as matrices filled with NaN values.

        Based only on the "current" results object (i.e. the Kalman smoother
        applied to the sample), there is not enough information to compute
        Cov(t, t+j) for the last `lag - 1` observations of the sample. However,
        the values can be computed for these time points using the transition
        equation of the state space representation, and so for time-invariant
        state space models we do compute these values. For time-varying models,
        this can also be done, but updated state space matrices for the
        out-of-sample time points must be provided via the `extend_kwargs`
        argument.

        See [1]_, Chapter 4.7, for all details about how these autocovariances
        are computed.

        The `t` and `start`/`end` parameters compute and return only the
        requested autocovariances. As a result, using these parameters is
        recommended to reduce the computational burden, particularly if the
        number of observations and/or the dimension of the state vector is
        large.

        References
        ----------
        .. [1] Durbin, James, and Siem Jan Koopman. 2012.
               Time Series Analysis by State Space Methods: Second Edition.
               Oxford University Press.
        '''
    def news(self, previous, t: Incomplete | None = None, start: Incomplete | None = None, end: Incomplete | None = None, revised: Incomplete | None = None, design: Incomplete | None = None, state_index: Incomplete | None = None):
        '''
        Compute the news and impacts associated with a data release

        Parameters
        ----------
        previous : SmootherResults
            Prior results object relative to which to compute the news. This
            results object must have identical state space representation for
            the prior sample period so that the only difference is that this
            results object has updates to the observed data.
        t : int, optional
            A specific period for which to compute the news. Cannot be used in
            combination with `start` or `end`.
        start : int, optional
            The start of the interval (inclusive) of news to compute. Cannot be
            used in combination with the `t` argument. Default is the last
            period of the sample (`nobs - 1`).
        end : int, optional
            The end of the interval (exclusive) of news to compute. Note that
            since it is an exclusive endpoint, the returned news do not include
            the value at this index. Cannot be used in combination with the `t`
            argument.
        design : array, optional
            Design matrix for the period `t` in time-varying models. If this
            model has a time-varying design matrix, and the argument `t` is out
            of this model\'s sample, then a new design matrix for period `t`
            must be provided. Unused otherwise.
        state_index : array_like, optional
            An optional index specifying a subset of states to use when
            constructing the impacts of revisions and news. For example, if
            `state_index=[0, 1]` is passed, then only the impacts to the
            observed variables arising from the impacts to the first two
            states will be returned.

        Returns
        -------
        news_results : SimpleNamespace
            News and impacts associated with a data release. Includes the
            following attributes:

            - `update_impacts`: update to forecasts of impacted variables from
              the news. It is equivalent to E[y^i | post] - E[y^i | revision],
              where y^i are the variables of interest. In [1]_, this is
              described as "revision" in equation (17).
            - `revision_impacts`: update to forecasts of variables impacted
              variables from data revisions. It is
              E[y^i | revision] - E[y^i | previous], and does not have a
              specific notation in [1]_, since there for simplicity they assume
              that there are no revisions.
            - `news`: the unexpected component of the updated data. Denoted
              I = y^u - E[y^u | previous], where y^u are the data points that
              were newly incorporated in a data release (but not including
              revisions to data points that already existed in the previous
              release). In [1]_, this is described as "news" in equation (17).
            - `revisions`
            - `gain`: the gain matrix associated with the "Kalman-like" update
              from the news, E[y I\'] E[I I\']^{-1}. In [1]_, this can be found
              in the equation For E[y_{k,t_k} \\mid I_{v+1}] in the middle of
              page 17.
            - `revision_weights`
            - `update_forecasts`: forecasts of the updated periods used to
              construct the news, E[y^u | previous].
            - `update_realized`: realizations of the updated periods used to
              construct the news, y^u.
            - `revised_prev`
            - `revised`
            - `prev_impacted_forecasts`: previous forecast of the periods of
              interest, E[y^i | previous].
            - `post_impacted_forecasts`: forecast of the periods of interest
              after taking into account both revisions and updates,
              E[y^i | post].
            - `revision_results`: results object that updates the `previous`
              results to take into account data revisions.
            - `revisions_ix`: list of `(t, i)` positions of revisions in endog
            - `updates_ix`: list of `(t, i)` positions of updates to endog

        Notes
        -----
        This method computes the effect of new data (e.g. from a new data
        release) on smoothed forecasts produced by a state space model, as
        described in [1]_. It also computes the effect of revised data on
        smoothed forecasts.

        References
        ----------
        .. [1] Bańbura, Marta and Modugno, Michele. 2010.
               "Maximum likelihood estimation of factor models on data sets
               with arbitrary pattern of missing data."
               No 1189, Working Paper Series, European Central Bank.
               https://EconPapers.repec.org/RePEc:ecb:ecbwps:20101189.
        .. [2] Bańbura, Marta, and Michele Modugno.
               "Maximum likelihood estimation of factor models on datasets with
               arbitrary pattern of missing data."
               Journal of Applied Econometrics 29, no. 1 (2014): 133-160.

        '''
    def smoothed_state_gain(self, updates_ix, t: Incomplete | None = None, start: Incomplete | None = None, end: Incomplete | None = None, extend_kwargs: Incomplete | None = None):
        """
        Cov(\\tilde \\alpha_{t}, I) Var(I, I)^{-1}

        where I is a vector of forecast errors associated with
        `update_indices`.

        Parameters
        ----------
        updates_ix : list
            List of indices `(t, i)`, where `t` denotes a zero-indexed time
            location and `i` denotes a zero-indexed endog variable.
        """
    @property
    def smoothed_forecasts(self): ...
    @property
    def smoothed_forecasts_error(self): ...
    @property
    def smoothed_forecasts_error_cov(self): ...
    def get_smoothed_decomposition(self, decomposition_of: str = 'smoothed_state', state_index: Incomplete | None = None):
        '''
        Decompose smoothed output into contributions from observations

        Parameters
        ----------
        decomposition_of : {"smoothed_state", "smoothed_signal"}
            The object to perform a decomposition of. If it is set to
            "smoothed_state", then the elements of the smoothed state vector
            are decomposed into the contributions of each observation. If it
            is set to "smoothed_signal", then the predictions of the
            observation vector based on the smoothed state vector are
            decomposed. Default is "smoothed_state".
        state_index : array_like, optional
            An optional index specifying a subset of states to use when
            constructing the decomposition of the "smoothed_signal". For
            example, if `state_index=[0, 1]` is passed, then only the
            contributions of observed variables to the smoothed signal arising
            from the first two states will be returned. Note that if not all
            states are used, the contributions will not sum to the smoothed
            signal. Default is to use all states.

        Returns
        -------
        data_contributions : array
            Contributions of observations to the decomposed object. If the
            smoothed state is being decomposed, then `data_contributions` are
            shaped `(nobs, k_states, nobs, k_endog)`, where the
            `(t, m, j, p)`-th element is the contribution of the `p`-th
            observation at time `j` to the `m`-th state at time `t`. If the
            smoothed signal is being decomposed, then `data_contributions` are
            shaped `(nobs, k_endog, nobs, k_endog)`, where the
            `(t, k, j, p)`-th element is the contribution of the `p`-th
            observation at time `j` to the smoothed prediction of the `k`-th
            observation at time `t`.
        obs_intercept_contributions : array
            Contributions of the observation intercept to the decomposed
            object. If the smoothed state is being decomposed, then
            `obs_intercept_contributions` are shaped
            `(nobs, k_states, nobs, k_endog)`, where the `(t, m, j, p)`-th
            element is the contribution of the `p`-th observation intercept at
            time `j` to the `m`-th state at time `t`. If the smoothed signal
            is being decomposed, then `obs_intercept_contributions` are shaped
            `(nobs, k_endog, nobs, k_endog)`, where the `(t, k, j, p)`-th
            element is the contribution of the `p`-th observation at time `j`
            to the smoothed prediction of the `k`-th observation at time `t`.
        state_intercept_contributions : array
            Contributions of the state intercept to the decomposed object. If
            the smoothed state is being decomposed, then
            `state_intercept_contributions` are shaped
            `(nobs, k_states, nobs, k_states)`, where the `(t, m, j, l)`-th
            element is the contribution of the `l`-th state intercept at
            time `j` to the `m`-th state at time `t`. If the smoothed signal
            is being decomposed, then `state_intercept_contributions` are
            shaped `(nobs, k_endog, nobs, k_endog)`, where the
            `(t, k, j, l)`-th element is the contribution of the `p`-th
            observation at time `j` to the smoothed prediction of the `k`-th
            observation at time `t`.
        prior_contributions : array
            Contributions of the prior to the decomposed object. If the
            smoothed state is being decomposed, then `prior_contributions` are
            shaped `(nobs, k_states, k_states)`, where the `(t, m, l)`-th
            element is the contribution of the `l`-th element of the prior
            mean to the `m`-th state at time `t`. If the smoothed signal is
            being decomposed, then `prior_contributions` are shaped
            `(nobs, k_endog, k_states)`, where the `(t, k, l)`-th
            element is the contribution of the `l`-th element of the prior mean
            to the smoothed prediction of the `k`-th observation at time `t`.

        Notes
        -----
        Denote the smoothed state at time :math:`t` by :math:`\\alpha_t`. Then
        the smoothed signal is :math:`Z_t \\alpha_t`, where :math:`Z_t` is the
        design matrix operative at time :math:`t`.
        '''
