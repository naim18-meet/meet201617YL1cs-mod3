from datetime import datetime
import datetime
def get_days_to_bday(year,month,day):
    now = datetime.date.today()
    bday = datetime.date(year,month,day)
    return str(bday - now )
