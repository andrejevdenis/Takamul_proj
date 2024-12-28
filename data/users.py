import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    email: str
    not_email: str
    message: str

test_user = User(
    first_name='Fedor',
    email='fedyaosminog@ramb',
    not_email='fedyaosminog@ramb',
    message='Just do it'
)