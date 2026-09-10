__all__ = ['egg_link_path_from_sys_path', 'egg_link_path_from_location']

def egg_link_path_from_sys_path(raw_name: str) -> str | None:
    """
    Look for a .egg-link file for project name, by walking sys.path.
    """
def egg_link_path_from_location(raw_name: str) -> str | None:
    """
    Return the path for the .egg-link file if it exists, otherwise, None.

    There's 3 scenarios:
    1) not in a virtualenv
       try to find in site.USER_SITE, then site_packages
    2) in a no-global virtualenv
       try to find in site_packages
    3) in a yes-global virtualenv
       try to find in site_packages, then site.USER_SITE
       (don't look in global location)

    For #1 and #3, there could be odd cases, where there's an egg-link in 2
    locations.

    This method will just return the first one found.
    """
