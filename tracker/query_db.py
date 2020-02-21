from .engine import session
from .models import Resume, Application, Status


# To-Do find a better solution to query the database for status
def get_applications(application_status):
    """
    Returns all applications
    :return: List of applications with type Application
    """
    # query DB for applications returns list of objects
    # Considered Valid Status: 0,1,4,5,6,8
    try:
        applications = session.query(Application)
    except:  # Broad exception to cover all basis for failure
        return "Applications were not retrieved from Database due to an error"

    valid_search_results = []
    for i in applications:
        if i.status in application_status:
            valid_search_results.append(i)
    return valid_search_results


def get_statuses():
    """
    Queries and returns the Status table for all available statuses
    """
    try:
        statuses = session.query(Status)
    except:
        return "An error has occured with fetching statuses"

    return statuses

