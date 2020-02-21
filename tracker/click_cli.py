import click
from .query_db import get_applications, get_statuses
from .insert_db import add_application

# To-Do List
# 1 Create a better to-do list
# 2 Need to be able to have some default options for status/ resume
# 3 Need to do validation when correcting for input
# 4 Show full status in show command not
# 5 Build update command for status
# 6 Auto add date? Build in method to override?
# 7 A GUI might be easier or web interface, just saying.


@click.group()
def main():
    """ Python CLI for adding job tracking to a database
    """
    click.echo("Welcome to Kyle's Job Tracker!")
    click.echo("Please use 'help' to see a detailed list of commands")
    pass


def _get_list():
    """
    :return: Returns the list of options to add from the database
    """
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

    return application_data

# Not implement
def _prompt(prompt):
    """
    Displays prompt to user for list of DB options.
    Not yet implemented.
    """
    pass


@main.command()
def add():
    """Add items into the database."""
    click.echo("Please follow the prompts to enter in application information")
    application_data = _get_list()

    for i in application_data:
        # Ask user for input for each one? Some how give more information
        application_data[i] = click.prompt("Please enter information for " + i)
    click.echo("You have selected the following, please confirm your entries")

    valid = False
    while not valid:
        # Get response form user to see if fields are valid
        for i in application_data:
            click.echo("Item: " + i + " Response: " + application_data[i])
        user_validation_response = click.prompt("Are these fields correct? [Y/n]")

        # Add or change fields based on user entry
        # TO-DO: Better try except statements, check for errors before adding.
        if user_validation_response == 'Y' or user_validation_response == 'y':
            # Store in DB and return response if failure or not
            click.echo("Submitting to DB, please stand by.")
            click.echo(".......")
            try:
                add_application(application_data)
            except Exception as e:
                click.echo("There was an error trying to add to the DB")
                click.echo("Error was" + e)
            valid = True
        elif user_validation_response == 'N' or user_validation_response == 'n':
            user_to_edit = click.prompt('Please enter the field you would like to edit (exact name)')
            try:
                application_data[user_to_edit] = click.prompt("Please enter information for " + user_to_edit)
            except:
                click.echo("Invalid selection")
        else:
            click.echo("I did not understand your response.")


@main.command()
def help():
    """
    Displays a dictionary of help commands
    :return: None
    """
    # Keep all the commands in the dictionary.
    cmd_dict = {
        'help': 'Help command to see more commands',
        'add': 'Adds an application to the DB type',
        'show': 'Prints current job applications with non rejection status'
    }
    click.echo("When using options with show you must give options an argument for valid commands")
    click.echo("Example: python jobtracker.py show -l 1")
    for i in cmd_dict:
        click.echo(" " + i + ": " + cmd_dict[i])


@main.command()
#@click.option("-id", "-new_status")
def update(app_id="", new_status=""):
    """
        Updates the status of a given job description.
    """
    click.echo("Use show to display a list of Applications, get its ID and use that to "
               "run the update command.")

    click.echo("You may update to the following statuses")
    _show_available_status()

    if app_id != "" and new_status != "":
        try:
            pass
        except:
            return "Was able to change the status of {id}.Please check your ID and status".format(id=app_id)


def _show_available_status():
    """
    Displays the current statuses avialble int he Status table
    """
    for i in get_statuses():
        click.echo("{sid} : {statement}".format(sid=i.id, statement=i.statement))


def _format_display_applications(applications):
    """
    prints out the applications past as arugment
    :args: list of Application objects
    """
    click.echo("Displaying all jobs with status of applied")
    click.echo("Company Name | Date Applied  | Resume Version "
               "| Position Applied | Status")
    for i in applications:
        click.echo(i.company_name + " | " + str(i.date_applied) + " | "
              + str(i.resume_version_id) + " | " +
              i.position + " | " + str(i.status))


@main.command()
def showvalid():
    search_status = [0, 1, 4, 5, 6, 8,]
    applications = get_applications(search_status)
    _format_display_applications(applications)


@main.command()
@click.argument("user_search_status")
def showcuststatus(user_search_status):
    _list_search_status = [int(user_search_status)]
    applications = get_applications(_list_search_status)
    _format_display_applications(applications)


@main.command()
@click.option("-h", "-l")
def showhelp(h=""):
    """Displays valid job applications. Valid is those with a non_rejection status
    :arg:
        -l: List out avaiable status to search from
        -h: Print help for this command
    :return None
    """
    click.echo("Will soon list out help and display a list of valid statuses to choose from")


if __name__ == '__main__':
    main()  # invokes the group decorator and any function with @click.command()
