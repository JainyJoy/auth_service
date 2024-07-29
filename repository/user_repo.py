from database import session_obj, User


class UserRepository:
    def __init__(self):
        pass

    def create_user(self, payload):
        """Create a user"""
        with session_obj() as session:
            user = User(**payload)
            session.add(user)
            session.commit()
            session.refresh(user)
        return True

    def get_user_by_email(self, email):
        """Get user by email"""
        with session_obj() as session:
            user = session.query(User).filter_by(email=email).first()
        return user

