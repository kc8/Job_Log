from sqlalchemy import Column, ForeignKey, Integer, String, Date
from .engine import engine, Base


class Application(Base):
    """
    Table Holds each application with date applied, Resume version etc.
    #To-Do
     - Want implement a cover letter field value similar to the resume and status tables
    """
    __tablename__ = 'application'
    # left out id to see if it auto generates a primary key
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=False, default="DEFAULT")
    date_applied = Column(Date, nullable=False)
    application_type = Column(String, nullable=True, default="Website")
    company_name = Column(String, nullable=False)
    person_contacted = Column(String, nullable=True, default='Employer')
    resume_version_id = Column(Integer, ForeignKey('resume.id'))
    # cover_letter_id = Column(Integer, ForeignKey ('cover_letter.id'))
    job_link = Column(String, nullable=True)
    status = Column(Integer, ForeignKey('status.id'))


class Status(Base):
    """
    Statuses for each Application
    Each Application has a status associated with it. Example "Applied" to a position or "Rejected" from a
    position.
    """
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    statement = Column(String, nullable=False)


class Resume(Base):
    """
    Resume tracker table. Each application has a specific Resume ID associated with it.
    This table keeps track of those version IDs
    """
    __tablename__ = 'resume'
    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    created = Column(Date, nullable=False)


Base.metadata.create_all(engine)

