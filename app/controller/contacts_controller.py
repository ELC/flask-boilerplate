from typing import List

from ..database import contact_db
from ..models.models import Contact
from ..helpers import helper


def create(contact_: Contact) -> Contact:
    contact = helper.format_name(contact_)
    helper.validate_contact(contact)
    return contact_db.create(contact)


def update(contact: Contact) -> Contact:
    contact = helper.format_name(contact)
    helper.validate_contact(contact)
    return contact_db.update(contact)


def delete(contact: Contact) -> Contact:
    return contact_db.delete(contact)


def lists() -> List[Contact]:
    return contact_db.list_all()


def details(contact: Contact) -> Contact:
    return contact_db.detail(contact)
