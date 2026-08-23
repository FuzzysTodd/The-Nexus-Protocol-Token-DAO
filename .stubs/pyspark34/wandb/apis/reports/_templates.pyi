from .util import coalesce as coalesce
from _typeshed import Incomplete

def create_example_header():
    """Create an example header with image at top."""
def create_example_footer():
    """Create an example footer with image and text at bottom."""
def create_enterprise_report(project: Incomplete | None = None, title: str = 'Untitled Report', description: str = '', header: Incomplete | None = None, body: Incomplete | None = None, footer: Incomplete | None = None):
    """Create an example enterprise report with a header and footer.

    Can be used to add custom branding to reports.
    """
def create_customer_landing_page(project: Incomplete | None = None, company_name: str = 'My Company', main_contact: str = 'My Contact (name@email.com)', slack_link: str = 'https://company.slack.com'):
    """Create an example customer landing page using data from Andrew's demo."""
