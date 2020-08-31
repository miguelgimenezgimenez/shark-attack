import re
def clean_activity(activity):
    swimming = ['swim', 'diving', 'dived', 'spear', 'standing', 'walking',
                'wading', 'bathing', 'floating', 'snorkeling', 'overboard', 'washing', 'treading', 'fell']

    surfing = ['board', 'surf', 'paddling', 'kanoeing',
               'kayak', 'rowing', 'canoe', 'sail', 'ski']

    try:

        if any(val in activity.lower() for val in swimming):
            return 'below_surface'
        if any(val in activity.lower() for val in surfing):
            return 'above_surface'
        if 'fish' in activity.lower():
            return 'fishing'
        return activity

    except Exception:
        return activity


def get_month(date):
    try:

        month = re.findall(
            r'jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|summer|fall|', date, flags=re.IGNORECASE)
        month = list(filter(None, month))
        if len(month):
            return month[0].lower()
        return None
    except TypeError:
        return None


def get_season(month):
    northern_summer = ['apr', 'may', 'jun', 'jul', 'aug', 'sep', 'summer']
    northern_winter = ['jan', 'feb', 'mar', 'oct', 'nov', 'dec', 'fall']

    if month in northern_summer:
        return 'northern_summer'
    if month in northern_winter:
        return 'northern_winter'


def get_data_by_season(df, season):
    return df[df['Season'] == season]


def get_data_by_country(df, country):
    return df[df['Country'] == country]


def fix_species_name(row):
    try:
        shark_type = re.search(r'^(.*) shark', row['Species '])
        if(shark_type):
            return shark_type.group(1).lower()
    except TypeError as e:
        return row['Species ']
    return row['Species ']
