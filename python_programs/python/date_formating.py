from datetime import datetime


class DateTransform(object):
    @staticmethod
    def change_date_format(dates):
        formated_dates = []
        dformat_list = ['%Y-%m-%d', '%m-%d-%Y', '%Y/%m/%d', '%d/%m/%Y']
        for dt in dates:
            if '/' in dt or '-' in dt:
                for dformat in dformat_list:
                    try:
                        str_date = datetime.strptime(dt, dformat).strftime('%Y%m%d')
                        formated_dates.append(str_date)
                    except ValueError as e:
                        pass
        return formated_dates


dates = DateTransform.change_date_format(["2010/03/30", "15/12/2016", "11-15-2012", "20130720"])
print dates
