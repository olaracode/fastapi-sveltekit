from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

# Create a ChatRoom model
# This model should have an id, a name


class ChatRoom(Base):
    __tablename__ = "chat_rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    creator_id = Column(Integer, ForeignKey("users.id"))
    participants = relationship(
        "ChatRoomParticipant", backref="chat_room")
    messages = relationship("Message", backref="chat_room")


class ChatRoomParticipant(Base):
    __tablename__ = "chat_room_participants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_room_id = Column(Integer, ForeignKey("chat_rooms.id"))


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    created_at = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_room_id = Column(Integer, ForeignKey("chat_rooms.id"))
