from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2',
    request_method='GET',
    permission=NO_PERMISSION_REQUIRED)
def home_view(request):
    return {}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_stock_portfolio_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
