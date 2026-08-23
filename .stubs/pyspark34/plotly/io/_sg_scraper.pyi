def plotly_sg_scraper(block, block_vars, gallery_conf, **kwargs):
    """Scrape Plotly figures for galleries of examples using
    sphinx-gallery.

    Examples should use ``plotly.io.show()`` to display the figure with
    the custom sphinx_gallery renderer.

    Since the sphinx_gallery renderer generates both html and static png
    files, we simply crawl these files and give them the appropriate path.

    Parameters
    ----------
    block : tuple
        A tuple containing the (label, content, line_number) of the block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery
    **kwargs : dict
        Additional keyword arguments to pass to
        :meth:`~matplotlib.figure.Figure.savefig`, e.g. ``format='svg'``.
        The ``format`` kwarg in particular is used to set the file extension
        of the output file (currently only 'png' and 'svg' are supported).

    Returns
    -------
    rst : str
        The ReSTructuredText that will be rendered to HTML containing
        the images.

    Notes
    -----
    Add this function to the image scrapers
    """
def figure_rst(figure_list, sources_dir):
    """Generate RST for a list of PNG filenames.

    Depending on whether we have one or more figures, we use a
    single rst call to 'image' or a horizontal list.

    Parameters
    ----------
    figure_list : list
        List of strings of the figures' absolute paths.
    sources_dir : str
        absolute path of Sphinx documentation sources

    Returns
    -------
    images_rst : str
        rst code to embed the images in the document
    """

SINGLE_HTML: str
