# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column,Integer,ForeignKey
class PrivateShare(Base):
    __tablename__ = "private_share"
    private_share_target_id = Column(Integer, ForeignKey("user.user_id"), primary_key=True)
    private_share_file_id = Column(Integer, ForeignKey("file.file_id"), primary_key=True)
    def __init__(self, fileId, targetId):
        self.private_share_file_id = fileId
        self.private_share_target_id = targetId
