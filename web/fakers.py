import factory
from dataclasses import dataclass


@dataclass
class Applicant:
    first_name: str
    last_name: str
    email: str
    phone: str
    link: str

    @property
    def dict(self):
        return self.__dict__


class RandomApplicantFactory(factory.Factory):
    class Meta:
        model = Applicant

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    link = factory.LazyAttribute(lambda o: '%s@linkdin.com' % o.first_name)

