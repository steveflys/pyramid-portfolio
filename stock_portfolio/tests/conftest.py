import os
import pytest
from pyramid import testing
from ..models.meta import Base
from ..models import Stock


@pytest.fixture
def test_stock():
    return Stock(
        symbol='WTF',
        companyName='Wha The Foo',
        CEO='Him',
        website='www.foobar.com',
        industry='yup',
        sector='9th',
        exchange='NYSE',
        issueType='cs',
        description='Does WTF he likes, when he likes'
    )


@pytest.fixture
def configuration(request):s
    """Setup a database for testing purposes."""
    config = testing.setUp(settings={
        # 'sqlalchecmy.url': 'postgres://localhost:5432/entries_test'
        'sqlalchemy.url': os.environ['TEST_DATABASE_URL']
    })
    config.include('stock_portfolio.models')
    config.include('stock_portfolio.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """Create a database session for interacting with the test database."""
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """Create a dummy GET request with a dbsession."""
    return testing.DummyRequest(dbsession=db_session)