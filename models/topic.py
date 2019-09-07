import time

from sqlalchemy import String, Integer, Column, Text, UnicodeText, Unicode

# from models import Model

from models.base_model import SQLMixin, db
from models.user import User
from models.reply import Reply
from models.board import Board
from utils import log


class Topic(SQLMixin, db.Model):
    views = Column(Integer, nullable=False, default=0)
    title = Column(Unicode(50), nullable=False)
    content = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, nullable=False)
    board_id = Column(Integer, nullable=False)

    # def user(self):
    #     u = User.one(id=self.user_id)
    #     return u


    def board(self):
        u = Board.one(id=self.board_id)
        return u

    @classmethod
    def new(cls, form, user_id):
        form['user_id'] = user_id
        m = super().new(form)
        return m

    @classmethod
    def get(cls, id):
        m = cls.one(id=id)
        m.views += 1
        m.save()
        return m

    @classmethod
    def delete(cls, id):
        # m = cls.one(id=id)
        Topic.query.filter_by(id=id).delete()
        Reply.query.filter_by(topic_id=id).delete()
        db.session.commit()

        # return m



    def user(self):
        u = User.one(id=self.user_id)
        return u

    def replies(self):
        ms = Reply.all(topic_id=self.id)
        return ms

    def reply_count(self):
        count = len(self.replies())
        return count

    def reply_user_time(self, user_id):
        # ts = Topic.query\
        #     .join(Reply, Topic.id==Reply.topic_id)\
        #     .filter(Reply.user_id==user_id)\
        #     .order_by(Reply.created_time.desc())\
        #     .limit(1)\
        #     .first()
        # return ts
        r = Reply.query\
            .join(Topic,Reply.topic_id==self.id)\
            .filter(Reply.user_id==user_id) \
            .order_by(Reply.created_time.desc()) \
            .limit(1) \
            .first()
        return r
        # r = Reply.query\
        #     .
        # ms = Reply.all(topic_id=self.id)
        # rs = []
        # for i in ms:
        #     # u = User.one(id=user_id)
        #     if user_id == i.user_id:
        #         rs.append(i)
        #
        # if rs == None:
        #     return rs
        # else:
        #     rs = sorted(rs, key=lambda m: m.created_time, reverse=True)
        #     return rs[0]

    def last_reply(self):
        r = Reply.query\
            .join(Topic,Reply.topic_id==self.id)\
            .filter(Reply.topic_id==self.id) \
            .order_by(Reply.created_time.desc()) \
            .limit(1) \
            .first()
        return r
    #
    #     rs = Reply.all(topic_id=self.id)
    #     ts = []
    #     for r in rs:
    #         # t = User.one(id=r.user_id)
    #         ts.append(r)
    #
    #     if ts == None:
    #         log('jinlail ')
    #         return ts
    #     else:
    #         log('liangwang')
    #         ts = sorted(ts, key=lambda m: m.created_time, reverse=True)
    #         # t = rs[0]
    #         # t = User.one(id=t.user_id)
    #         return ts[0]
        # ts = Topic.query\
        #     .join(Reply, Topic.id==Reply.topic_id)\
        #     .filter(Reply.user_id==user_id)\
        #     .all()
        # return ts



