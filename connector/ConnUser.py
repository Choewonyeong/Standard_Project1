from setting import Path
from sqlite3 import connect
from pandas import DataFrame


class ConnUser:
    def __init__(self):
        self.path = Path.pathUser

    def ReturnUserIds(self):
        sql = "Select `아이디` From User;"
        conn = connect(self.path)
        query = conn.execute(sql)
        userIds = [userId[0] for userId in query.fetchall()]
        conn.close()
        return userIds

    def ReturnUserPassword(self, userId):
        try:
            sql = f"Select `비밀번호` From User Where `아이디`='{userId}';"
            conn = connect(self.path)
            query = conn.execute(sql)
            userPassword = query.fetchone()[0]
            conn.close()
            return userPassword
        except Exception as e:
            print(e)
            return 'No Password Where UserID'

    def ReturnUserAuthor(self, userId):
        try:
            sql = f"Select `권한설정` From User Where `아이디`='{userId}';"
            conn = connect(self.path)
            query = conn.execute(sql)
            userAuthor = query.fetchone()[0]
            conn.close()
            return userAuthor
        except Exception as e:
            print(e)
            return '사용자'

    def ReturnUserName(self, userId):
        sql = f"Select `성명` From User Where `아이디`='{userId}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            userName = query.fetchone()[0]
            conn.close()
            return userName
        except Exception as e:
            print(e)
            return ''

    def ReturnUserInfo(self, userId):
        sql = f"Select `아이디`, `성명`, `비밀번호` From User Where `아이디`='{userId}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            userName = list(query.fetchall()[0])
            conn.close()
            return userName
        except Exception as e:
            print(e)
            return ''

    def ReturnApproval(self, userId):
        sql = f"Select `승인여부` From User Where `아이디`='{userId}';"
        try:
            conn = connect(self.path)
            query = conn.execute(sql)
            approval = query.fetchone()[0]
            conn.close()
            return approval
        except Exception as e:
            print(e)
            return '거절'

    def UpdatePassword(self, userPassword, userId):
        sql = f"Update User Set `비밀번호`='{userPassword}' Where `아이디`='{userId}';"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.UpdatePassword(userPassword, userId):
                    break

    def InsertUserInfo(self, userId, userName, userPassword):
        sql = f"Insert Into User(`아이디`, `성명`, `비밀번호`) Values('{userId}','{userName}','{userPassword}');"
        try:
            conn = connect(self.path)
            conn.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            while True:
                if self.InsertUserInfo(userId, userName, userPassword):
                    break

    def ColumnAndDfUser(self):
        sql = "Select * From User;"
        conn = connect(self.path)
        query = conn.execute(sql)
        columns = [column[0] for column in query.description]
        query = conn.execute(sql)
        dfUser = DataFrame(data=query.fetchall(), columns=columns)
        conn.close()
        return columns, dfUser
