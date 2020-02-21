from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, backref, relationship
from .models import Resume, Application, Status
from .engine import session


# Need to sanitize/check for validity in user input
def add_status(id, statement):
    """
    Add a single status into the Database.
    :param id: Manual ID in the database, query DB to find next available
    :param statement: The String statement of Status 'Application Submitted'
    :return: Returns nothing. SQLAlchemy will through an error.
    """
    status = Status(id=id,
                    statement=statement
    )
    session.add(status)
    session.commit()


def _add_original_status():
    """
    function used to populate teh database with the original status table. Original is below.
    This function should not be used or called unless changing databases or adding new statuses
    status_table = {
        '0': 'Applied',
        '1': 'Conducting Phone Interview',
        '2': 'No Response',
        '4': 'Waiting to hear back',
        '5': 'Conducted On Site Interview',
        '6': 'Offered Proposed',
        '7': 'Offered Declined',
        '8': 'Offered Accepted',
        '9': 'Did not get
    }
    """
    # Create a blank/fake list in case function is called:
    status_table = list('')
    for x in status_table:
        add_status(x, status_table[x])


# Need to sanitize/check for validity in user input
def add_resume(id, link, date_created):
    """
    Add a Resume version into the database
    :param id: ID of the Resume (usually date created in a string)
    :param link: Google Drive URL to Resume
    :param date_created: Date created as a date object
    :return: None will through error if SQLAlchemy errors out
    """
    resume = Resume(id=id,
                    link=link,
                    created=date_created
                    )
    session.add(resume)
    session.commit()


# Need to sanitize/check for validity in user input
def add_application(application_data):
    """
    Adds an application to the database. Needs a dictionary of data.

    Accepts dictionary structure:
        application_data = {
        'position': '',
        'date_applied': '',
        'application_type': '',
        'company_name': '',
        'person_contacted': '',
        'resume_version_id': '',
        'job_link': '',
        'status': '',
    }
    :param application_data: Dictionary of application data.
    :return: None, will through error if SQL alechemy errors out
    """
    application = Application(
        date_applied=application_data['date_applied'],
        application_type=application_data['application_type'],
        company_name=application_data['company_name'],
        person_contacted=application_data['person_contacted'],
        resume_version_id=application_data['resume_version_id'],
        job_link=application_data['job_link'],
        position=application_data['position'],
        status=application_data['status']
        )

    session.add(application)
    session.commit()


def update_status():
    """
    Updates the status of teh application
    """
    pass