import json
import datetime
from bottle import route, request, template, run
import requests


class ResponseDto:

    def __init__(self, year, month, salary, hour_income):
        self.year = year
        self.month = self.convert_month_to_str(month)
        self.salary = salary
        self.hour_income = hour_income

    def convert_month_to_str(self, month):
        return datetime.date(1900, month, 1).strftime('%B').upper()


class WorkDaysService:
    
    IS_DAY_OFF_URL = 'https://isdayoff.ru/api/getdata'

    def get_work_days(self, year, month):
        params = {'year': year, 'month': month}
        return requests.get(self.IS_DAY_OFF_URL, params=params).text.count('0')


class HourIncomeCounter:

    def __init__(self, work_days_service: WorkDaysService):
        self.work_days_service = work_days_service

    def count_hour_income(self, year, month, salary):
        return round(salary / (self.work_days_service.get_work_days(year, month) * 8), 2)


counter = HourIncomeCounter(WorkDaysService())


@route('/salary')
def count_hour_salary():
    year, month, salary = int(request.query.year), int(request.query.month), float(request.query.salary)
    hour_income = counter.count_hour_income(year, month, salary)
    response = ResponseDto(year, month, salary, hour_income)
    return template(json.dumps(response.__dict__, indent=4))


def main():
    run(host='localhost', port=8080)


if __name__ == "__main__":
    main()
