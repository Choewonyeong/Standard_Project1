from sqlite3 import connect
from setting import Path
from pandas import DataFrame


class ConnOption:
    def __init__(self):
        self.path = Path.pathOption

    def ColumnAndDfOption(self):
        sql = "Select * from Option"
        conn = connect(self.path)
        query = conn.execute(sql)
        columns = [column[0] for column in query.description]
        query = conn.execute(sql)
        df = DataFrame(data=query.fetchall(), columns=columns)
        conn.close()
        return columns, df

    def ReturnMainOption(self):
        sql = "Select `심사항목` from Option"
        conn = connect(self.path)
        query = conn.execute(sql)
        mainOptions = [option[0] for option in query.fetchall()]
        conn.close()
        return mainOptions

    def ReturnSummary(self):
        sql = "Select `개요` from Option"
        conn = connect(self.path)
        query = conn.execute(sql)
        summaries = [summary[0] for summary in query.fetchall()]
        conn.close()
        return summaries

    def ReturnDetail(self):
        sql = "Select `세부항목` from Option"
        conn = connect(self.path)
        query = conn.execute(sql)
        details = [detail[0] for detail in query.fetchall()]
        conn.close()
        return details

    def ReturnPoint(self):
        sql = "Select `배점` from Option"
        conn = connect(self.path)
        query = conn.execute(sql)
        points = [point[0] for point in query.fetchall()]
        conn.close()
        return points

    def ReturnPs(self):
        sql = "Select `비고` from Option"
        conn = connect(self.path)
        query = conn.execute(sql)
        ps = [p[0] for p in query.fetchall()]
        conn.close()
        return ps
