from _typeshed import Incomplete
from statsmodels.iolib.summary import Summary as Summary
from statsmodels.iolib.table import SimpleTable as SimpleTable
from statsmodels.iolib.tableformatting import fmt_params as fmt_params

class NewsResults:
    '''
    Impacts of data revisions and news on estimates of variables of interest

    Parameters
    ----------
    news_results : SimpleNamespace instance
        Results from `KalmanSmoother.news`.
    model : MLEResults
        The results object associated with the model from which the NewsResults
        was generated.
    updated : MLEResults
        The results object associated with the model containing the updated
        dataset.
    previous : MLEResults
        The results object associated with the model containing the previous
        dataset.
    impacted_variable : str, list, array, or slice, optional
        Observation variable label or slice of labels specifying particular
        impacted variables to display in output. The impacted variable(s)
        describe the variables that were *affected* by the news. If you do not
        know the labels for the variables, check the `endog_names` attribute of
        the model instance.
    tolerance : float, optional
        The numerical threshold for determining zero impact. Default is that
        any impact less than 1e-10 is assumed to be zero.
    row_labels : iterable
        Row labels (often dates) for the impacts of the revisions and news.

    Attributes
    ----------
    total_impacts : pd.Series
        Updates to forecasts of impacted variables from both news and data
        revisions, E[y^i | post] - E[y^i | previous].
    update_impacts : pd.Series
        Updates to forecasts of impacted variables from the news,
        E[y^i | post] - E[y^i | revisions] where y^i are the impacted variables
        of interest.
    revision_impacts : pd.Series
        Updates to forecasts of impacted variables from data revisions,
        E[y^i | revisions] - E[y^i | previous].
    news : pd.Series
        The unexpected component of the updated data,
        E[y^u | post] - E[y^u | revisions] where y^u are the updated variables.
    weights : pd.Series
        Weights describing the effect of news on variables of interest.
    revisions : pd.Series
        The revisions betwen the current and previously observed data
        y^r_{revised} - y^r_{previous} where y^r are the revised variables.
    revision_weights : pd.Series
        Weights describing the effect of revisions on variables of interest.
    update_forecasts : pd.Series
        Forecasts based on the previous dataset of the variables that were
        updated, E[y^u | previous].
    update_realized : pd.Series
        Actual observed data associated with the variables that were
        updated, y^u
    revised_prev : pd.Series
        Previously observed data associated with the variables that were
        revised, y^r_{previous}
    revised : pd.Series
        Currently observed data associated with the variables that were
        revised, y^r_{revised}
    prev_impacted_forecasts : pd.Series
        Previous forecast of the variables of interest, E[y^i | previous].
    post_impacted_forecasts : pd.Series
        Forecast of the variables of interest after taking into account both
        revisions and updates, E[y^i | post].
    revisions_iloc : pd.DataFrame
        The integer locations of the data revisions in the dataset.
    revisions_ix : pd.DataFrame
        The label-based locations of the data revisions in the dataset.
    updates_iloc : pd.DataFrame
        The integer locations of the updated data points.
    updates_ix : pd.DataFrame
        The label-based locations of updated data points.
    state_index : array_like
        Index of state variables used to compute impacts.

    References
    ----------
    .. [1] Bańbura, Marta, and Michele Modugno.
           "Maximum likelihood estimation of factor models on datasets with
           arbitrary pattern of missing data."
           Journal of Applied Econometrics 29, no. 1 (2014): 133-160.
    .. [2] Bańbura, Marta, Domenico Giannone, and Lucrezia Reichlin.
           "Nowcasting."
           The Oxford Handbook of Economic Forecasting. July 8, 2011.
    .. [3] Bańbura, Marta, Domenico Giannone, Michele Modugno, and Lucrezia
           Reichlin.
           "Now-casting and the real-time data flow."
           In Handbook of economic forecasting, vol. 2, pp. 195-237.
           Elsevier, 2013.
    '''
    model: Incomplete
    updated: Incomplete
    previous: Incomplete
    news_results: Incomplete
    row_labels: Incomplete
    params: Incomplete
    endog_names: Incomplete
    k_endog: Incomplete
    post_impacted_forecasts: Incomplete
    prev_impacted_forecasts: Incomplete
    update_impacts: Incomplete
    revision_impacts: Incomplete
    total_impacts: Incomplete
    revisions_iloc: Incomplete
    revisions_ix: Incomplete
    updates_iloc: Incomplete
    updates_ix: Incomplete
    state_index: Incomplete
    news: Incomplete
    revisions: Incomplete
    update_forecasts: Incomplete
    revised: Incomplete
    revised_prev: Incomplete
    update_realized: Incomplete
    weights: Incomplete
    revision_weights: Incomplete
    def __init__(self, news_results, model, updated, previous, impacted_variable: Incomplete | None = None, tolerance: float = 1e-10, row_labels: Incomplete | None = None) -> None: ...
    @property
    def impacted_variable(self): ...
    @impacted_variable.setter
    def impacted_variable(self, value) -> None: ...
    @property
    def tolerance(self): ...
    @tolerance.setter
    def tolerance(self, value) -> None: ...
    @property
    def data_revisions(self):
        """
        Revisions to data points that existed in the previous dataset

        Returns
        -------
        data_revisions : pd.DataFrame
            Index is as MultiIndex consisting of `revision date` and
            `revised variable`. The columns are:

            - `observed (prev)`: the value of the data as it was observed
              in the previous dataset.
            - `revised`: the revised value of the data, as it is observed
              in the new dataset

        See also
        --------
        data_updates
        """
    @property
    def data_updates(self):
        """
        Updated data; new entries that did not exist in the previous dataset

        Returns
        -------
        data_updates : pd.DataFrame
            Index is as MultiIndex consisting of `update date` and
            `updated variable`. The columns are:

            - `forecast (prev)`: the previous forecast of the new entry,
              based on the information available in the previous dataset
              (recall that for these updated data points, the previous dataset
              had no observed value for them at all)
            - `observed`: the value of the new entry, as it is observed in the
              new dataset

        See also
        --------
        data_revisions
        """
    @property
    def details_by_impact(self):
        """
        Details of forecast revisions from news, organized by impacts first

        Returns
        -------
        details : pd.DataFrame
            Index is as MultiIndex consisting of:

            - `impact date`: the date of the impact on the variable of interest
            - `impacted variable`: the variable that is being impacted
            - `update date`: the date of the data update, that results in
              `news` that impacts the forecast of variables of interest
            - `updated variable`: the variable being updated, that results in
              `news` that impacts the forecast of variables of interest

            The columns are:

            - `forecast (prev)`: the previous forecast of the new entry,
              based on the information available in the previous dataset
            - `observed`: the value of the new entry, as it is observed in the
              new dataset
            - `news`: the news associated with the update (this is just the
              forecast error: `observed` - `forecast (prev)`)
            - `weight`: the weight describing how the `news` effects the
              forecast of the variable of interest
            - `impact`: the impact of the `news` on the forecast of the
              variable of interest

        Notes
        -----
        This table decomposes updated forecasts of variables of interest from
        the `news` associated with each updated datapoint from the new data
        release.

        This table does not summarize the impacts or show the effect of
        revisions. That information can be found in the `impacts` or
        `revision_details_by_impact` tables.

        This form of the details table is organized so that the impacted
        dates / variables are first in the index. This is convenient for
        slicing by impacted variables / dates to view the details of data
        updates for a particular variable or date.

        However, since the `forecast (prev)` and `observed` columns have a lot
        of duplication, printing the entire table gives a result that is less
        easy to parse than that produced by the `details_by_update` property.
        `details_by_update` contains the same information but is organized to
        be more convenient for displaying the entire table of detailed updates.
        At the same time, `details_by_update` is less convenient for
        subsetting.

        See Also
        --------
        details_by_update
        revision_details_by_update
        impacts
        """
    @property
    def revision_details_by_impact(self):
        """
        Details of forecast revisions from revised data, organized by impacts

        Returns
        -------
        details : pd.DataFrame
            Index is as MultiIndex consisting of:

            - `impact date`: the date of the impact on the variable of interest
            - `impacted variable`: the variable that is being impacted
            - `revision date`: the date of the data revision, that results in
              `revision` that impacts the forecast of variables of interest
            - `revised variable`: the variable being revised, that results in
              `news` that impacts the forecast of variables of interest

            The columns are:

            - `observed (prev)`: the previous value of the observation, as it
              was given in the previous dataset
            - `revised`: the value of the revised entry, as it is observed in
              the new dataset
            - `revision`: the revision (this is `revised` - `observed (prev)`)
            - `weight`: the weight describing how the `revision` effects the
              forecast of the variable of interest
            - `impact`: the impact of the `revision` on the forecast of the
              variable of interest

        Notes
        -----
        This table decomposes updated forecasts of variables of interest from
        the `revision` associated with each revised datapoint from the new data
        release.

        This table does not summarize the impacts or show the effect of
        new datapoints. That information can be found in the
        `impacts` or `details_by_impact` tables.

        This form of the details table is organized so that the impacted
        dates / variables are first in the index. This is convenient for
        slicing by impacted variables / dates to view the details of data
        updates for a particular variable or date.

        However, since the `observed (prev)` and `revised` columns have a lot
        of duplication, printing the entire table gives a result that is less
        easy to parse than that produced by the `details_by_revision` property.
        `details_by_revision` contains the same information but is organized to
        be more convenient for displaying the entire table of detailed
        revisions. At the same time, `details_by_revision` is less convenient
        for subsetting.

        See Also
        --------
        details_by_revision
        details_by_impact
        impacts
        """
    @property
    def details_by_update(self):
        """
        Details of forecast revisions from news, organized by updates first

        Returns
        -------
        details : pd.DataFrame
            Index is as MultiIndex consisting of:

            - `update date`: the date of the data update, that results in
              `news` that impacts the forecast of variables of interest
            - `updated variable`: the variable being updated, that results in
              `news` that impacts the forecast of variables of interest
            - `forecast (prev)`: the previous forecast of the new entry,
              based on the information available in the previous dataset
            - `observed`: the value of the new entry, as it is observed in the
              new dataset
            - `impact date`: the date of the impact on the variable of interest
            - `impacted variable`: the variable that is being impacted

            The columns are:

            - `news`: the news associated with the update (this is just the
              forecast error: `observed` - `forecast (prev)`)
            - `weight`: the weight describing how the `news` affects the
              forecast of the variable of interest
            - `impact`: the impact of the `news` on the forecast of the
              variable of interest

        Notes
        -----
        This table decomposes updated forecasts of variables of interest from
        the `news` associated with each updated datapoint from the new data
        release.

        This table does not summarize the impacts or show the effect of
        revisions. That information can be found in the `impacts` table.

        This form of the details table is organized so that the updated
        dates / variables are first in the index, and in this table the index
        also contains the forecasts and observed values of the updates. This is
        convenient for displaying the entire table of detailed updates because
        it allows sparsifying duplicate entries.

        However, since it includes forecasts and observed values in the index
        of the table, it is not convenient for subsetting by the variable of
        interest. Instead, the `details_by_impact` property is organized to
        make slicing by impacted variables / dates easy. This allows, for
        example, viewing the details of data updates on a particular variable
        or date of interest.

        See Also
        --------
        details_by_impact
        impacts
        """
    @property
    def revision_details_by_update(self):
        """
        Details of forecast revisions from revisions, organized by updates

        Returns
        -------
        details : pd.DataFrame
            Index is as MultiIndex consisting of:

            - `revision date`: the date of the data revision, that results in
              `revision` that impacts the forecast of variables of interest
            - `revised variable`: the variable being revised, that results in
              `news` that impacts the forecast of variables of interest
            - `observed (prev)`: the previous value of the observation, as it
              was given in the previous dataset
            - `revised`: the value of the revised entry, as it is observed in
              the new dataset
            - `impact date`: the date of the impact on the variable of interest
            - `impacted variable`: the variable that is being impacted

            The columns are:

            - `revision`: the revision (this is `revised` - `observed (prev)`)
            - `weight`: the weight describing how the `revision` affects the
              forecast of the variable of interest
            - `impact`: the impact of the `revision` on the forecast of the
              variable of interest

        Notes
        -----
        This table decomposes updated forecasts of variables of interest from
        the `revision` associated with each revised datapoint from the new data
        release.

        This table does not summarize the impacts or show the effect of
        revisions. That information can be found in the `impacts` table.

        This form of the details table is organized so that the revision
        dates / variables are first in the index, and in this table the index
        also contains the previously observed and revised values. This is
        convenient for displaying the entire table of detailed revisions
        because it allows sparsifying duplicate entries.

        However, since it includes previous observations and revisions in the
        index of the table, it is not convenient for subsetting by the variable
        of interest. Instead, the `revision_details_by_impact` property is
        organized to make slicing by impacted variables / dates easy. This
        allows, for example, viewing the details of data revisions on a
        particular variable or date of interest.

        See Also
        --------
        details_by_impact
        impacts
        """
    @property
    def impacts(self):
        """
        Impacts from news and revisions on all dates / variables of interest

        Returns
        -------
        impacts : pd.DataFrame
            Index is as MultiIndex consisting of:

            - `impact date`: the date of the impact on the variable of interest
            - `impacted variable`: the variable that is being impacted

            The columns are:

            - `estimate (prev)`: the previous estimate / forecast of the
              date / variable of interest.
            - `impact of revisions`: the impact of all data revisions on
              the estimate of the date / variable of interest.
            - `impact of news`: the impact of all news on the estimate of
              the date / variable of interest.
            - `total impact`: the total impact of both revisions and news on
              the estimate of the date / variable of interest.
            - `estimate (new)`: the new estimate / forecast of the
              date / variable of interest after taking into account the effects
              of the revisions and news.

        Notes
        -----
        This table decomposes updated forecasts of variables of interest into
        the overall effect from revisions and news.

        This table does not break down the detail by the updated
        dates / variables. That information can be found in the
        `details_by_impact` `details_by_update` tables.

        See Also
        --------
        details_by_impact
        details_by_update
        """
    def summary_impacts(self, impact_date: Incomplete | None = None, impacted_variable: Incomplete | None = None, groupby: str = 'impact date', show_revisions_columns: Incomplete | None = None, sparsify: bool = True, float_format: str = '%.2f'):
        """
        Create summary table with detailed impacts from news; by date, variable

        Parameters
        ----------
        impact_date : int, str, datetime, list, array, or slice, optional
            Observation index label or slice of labels specifying particular
            impact periods to display. The impact date(s) describe the periods
            in which impacted variables were *affected* by the news. If this
            argument is given, the output table will only show this impact date
            or dates. Note that this argument is passed to the Pandas `loc`
            accessor, and so it should correspond to the labels of the model's
            index. If the model was created with data in a list or numpy array,
            then these labels will be zero-indexes observation integers.
        impacted_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying particular
            impacted variables to display. The impacted variable(s) describe
            the variables that were *affected* by the news. If you do not know
            the labels for the variables, check the `endog_names` attribute of
            the model instance.
        groupby : {impact date, impacted date}
            The primary variable for grouping results in the impacts table. The
            default is to group by update date.
        show_revisions_columns : bool, optional
            If set to False, the impacts table will not show the impacts from
            data revisions or the total impacts. Default is to show the
            revisions and totals columns if any revisions were made and
            otherwise to hide them.
        sparsify : bool, optional, default True
            Set to False for the table to include every one of the multiindex
            keys at each row.
        float_format : str, optional
            Formatter format string syntax for converting numbers to strings.
            Default is '%.2f'.

        Returns
        -------
        impacts_table : SimpleTable
            Table describing total impacts from both revisions and news. See
            the documentation for the `impacts` attribute for more details
            about the index and columns.

        See Also
        --------
        impacts
        """
    def summary_details(self, source: str = 'news', impact_date: Incomplete | None = None, impacted_variable: Incomplete | None = None, update_date: Incomplete | None = None, updated_variable: Incomplete | None = None, groupby: str = 'update date', sparsify: bool = True, float_format: str = '%.2f', multiple_tables: bool = False):
        '''
        Create summary table with detailed impacts; by date, variable

        Parameters
        ----------
        source : {news, revisions}
            The source of impacts to summarize. Default is "news".
        impact_date : int, str, datetime, list, array, or slice, optional
            Observation index label or slice of labels specifying particular
            impact periods to display. The impact date(s) describe the periods
            in which impacted variables were *affected* by the news. If this
            argument is given, the output table will only show this impact date
            or dates. Note that this argument is passed to the Pandas `loc`
            accessor, and so it should correspond to the labels of the model\'s
            index. If the model was created with data in a list or numpy array,
            then these labels will be zero-indexes observation integers.
        impacted_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying particular
            impacted variables to display. The impacted variable(s) describe
            the variables that were *affected* by the news. If you do not know
            the labels for the variables, check the `endog_names` attribute of
            the model instance.
        update_date : int, str, datetime, list, array, or slice, optional
            Observation index label or slice of labels specifying particular
            updated periods to display. The updated date(s) describe the
            periods in which the new data points were available that generated
            the news). See the note on `impact_date` for details about what
            these labels are.
        updated_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying particular
            updated variables to display. The updated variable(s) describe the
            variables that were *affected* by the news. If you do not know the
            labels for the variables, check the `endog_names` attribute of the
            model instance.
        groupby : {update date, updated date, impact date, impacted date}
            The primary variable for grouping results in the details table. The
            default is to group by update date.
        sparsify : bool, optional, default True
            Set to False for the table to include every one of the multiindex
            keys at each row.
        float_format : str, optional
            Formatter format string syntax for converting numbers to strings.
            Default is \'%.2f\'.
        multiple_tables : bool, optional
            If set to True, this function will return a list of tables, one
            table for each of the unique `groupby` levels. Default is False,
            in which case this function returns a single table.

        Returns
        -------
        details_table : SimpleTable or list of SimpleTable
            Table or list of tables describing how the news from each update
            (i.e. news from a particular variable / date) translates into
            changes to the forecasts of each impacted variable variable / date.

            This table contains information about the updates and about the
            impacts. Updates are newly observed datapoints that were not
            available in the previous results set. Each update leads to news,
            and the news may cause changes in the forecasts of the impacted
            variables. The amount that a particular piece of news (from an
            update to some variable at some date) impacts a variable at some
            date depends on weights that can be computed from the model
            results.

            The data contained in this table that refer to updates are:

            - `update date` : The date at which a new datapoint was added.
            - `updated variable` : The variable for which a new datapoint was
              added.
            - `forecast (prev)` : The value that had been forecast by the
              previous model for the given updated variable and date.
            - `observed` : The observed value of the new datapoint.
            - `news` : The news is the difference between the observed value
              and the previously forecast value for a given updated variable
              and date.

            The data contained in this table that refer to impacts are:

            - `impact date` : A date associated with an impact.
            - `impacted variable` : A variable that was impacted by the news.
            - `weight` : The weight of news from a given `update date` and
              `update variable` on a given `impacted variable` at a given
              `impact date`.
            - `impact` : The revision to the smoothed estimate / forecast of
              the impacted variable at the impact date based specifically on
              the news generated by the `updated variable` at the
              `update date`.

        See Also
        --------
        details_by_impact
        details_by_update
        '''
    def summary_revisions(self, sparsify: bool = True):
        """
        Create summary table showing revisions to the previous results' data

        Parameters
        ----------
        sparsify : bool, optional, default True
            Set to False for the table to include every one of the multiindex
            keys at each row.

        Returns
        -------
        revisions_table : SimpleTable
            Table showing revisions to the previous results' data. Columns are:

            - `revision date` : date associated with a revised data point
            - `revised variable` : variable that was revised at `revision date`
            - `observed (prev)` : the observed value prior to the revision
            - `revised` : the new value after the revision
            - `revision` : the new value after the revision
        """
    def summary_news(self, sparsify: bool = True):
        """
        Create summary table showing news from new data since previous results

        Parameters
        ----------
        sparsify : bool, optional, default True
            Set to False for the table to include every one of the multiindex
            keys at each row.

        Returns
        -------
        updates_table : SimpleTable
            Table showing new datapoints that were not in the previous results'
            data. Columns are:

            - `update date` : date associated with a new data point.
            - `updated variable` : variable for which new data was added at
              `update date`.
            - `forecast (prev)` : the forecast value for the updated variable
              at the update date in the previous results object (i.e. prior to
              the data being available).
            - `observed` : the observed value of the new datapoint.

        See Also
        --------
        data_updates
        """
    def summary(self, impact_date: Incomplete | None = None, impacted_variable: Incomplete | None = None, update_date: Incomplete | None = None, updated_variable: Incomplete | None = None, revision_date: Incomplete | None = None, revised_variable: Incomplete | None = None, impacts_groupby: str = 'impact date', details_groupby: str = 'update date', show_revisions_columns: Incomplete | None = None, sparsify: bool = True, include_details_tables: Incomplete | None = None, include_revisions_tables: bool = False, float_format: str = '%.2f'):
        '''
        Create summary tables describing news and impacts

        Parameters
        ----------
        impact_date : int, str, datetime, list, array, or slice, optional
            Observation index label or slice of labels specifying particular
            impact periods to display. The impact date(s) describe the periods
            in which impacted variables were *affected* by the news. If this
            argument is given, the impact and details tables will only show
            this impact date or dates. Note that this argument is passed to the
            Pandas `loc` accessor, and so it should correspond to the labels of
            the model\'s index. If the model was created with data in a list or
            numpy array, then these labels will be zero-indexes observation
            integers.
        impacted_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying particular
            impacted variables to display. The impacted variable(s) describe
            the variables that were *affected* by the news. If you do not know
            the labels for the variables, check the `endog_names` attribute of
            the model instance.
        update_date : int, str, datetime, list, array, or slice, optional
            Observation index label or slice of labels specifying particular
            updated periods to display. The updated date(s) describe the
            periods in which the new data points were available that generated
            the news). See the note on `impact_date` for details about what
            these labels are.
        updated_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying particular
            updated variables to display. The updated variable(s) describe the
            variables that newly added in the updated dataset and which
            generated the news. If you do not know the labels for the
            variables, check the `endog_names` attribute of the model instance.
        revision_date : int, str, datetime, list, array, or slice, optional
            Observation index label or slice of labels specifying particular
            revision periods to display. The revision date(s) describe the
            periods in which the data points were revised. See the note on
            `impact_date` for details about what these labels are.
        revised_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying particular
            revised variables to display. The updated variable(s) describe the
            variables that were *revised*. If you do not know the labels for
            the variables, check the `endog_names` attribute of the model
            instance.
        impacts_groupby : {impact date, impacted date}
            The primary variable for grouping results in the impacts table. The
            default is to group by update date.
        details_groupby : str
            One of "update date", "updated date", "impact date", or
            "impacted date". The primary variable for grouping results in the
            details table. Only used if the details tables are included. The
            default is to group by update date.
        show_revisions_columns : bool, optional
            If set to False, the impacts table will not show the impacts from
            data revisions or the total impacts. Default is to show the
            revisions and totals columns if any revisions were made and
            otherwise to hide them.
        sparsify : bool, optional, default True
            Set to False for the table to include every one of the multiindex
            keys at each row.
        include_details_tables : bool, optional
            If set to True, the summary will show tables describing the details
            of how news from specific updates translate into specific impacts.
            These tables can be very long, particularly in cases where there
            were many updates and in multivariate models. The default is to
            show detailed tables only for univariate models.
        include_revisions_tables : bool, optional
            If set to True, the summary will show tables describing the
            revisions and updates that lead to impacts on variables of
            interest.
        float_format : str, optional
            Formatter format string syntax for converting numbers to strings.
            Default is \'%.2f\'.

        Returns
        -------
        summary_tables : Summary
            Summary tables describing news and impacts. Basic tables include:

            - A table with general information about the sample.
            - A table describing the impacts of revisions and news.
            - Tables describing revisions in the dataset since the previous
              results set (unless `include_revisions_tables=False`).

            In univariate models or if `include_details_tables=True`, one or
            more tables will additionally be included describing the details
            of how news from specific updates translate into specific impacts.

        See Also
        --------
        summary_impacts
        summary_details
        summary_revisions
        summary_updates
        '''
    def get_details(self, include_revisions: bool = True, include_updates: bool = True): ...
    def get_impacts(self, groupby: Incomplete | None = None, include_revisions: bool = True, include_updates: bool = True): ...
