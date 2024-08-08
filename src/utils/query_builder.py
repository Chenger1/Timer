from sqlalchemy.sql.expression import and_


def convert_dict_to_sqlalchemy_filters(models_class, filters: dict):
    sql_alchemy_filters = []
    for key, value in filters.items():
        attr = getattr(models_class, key, None)
        if attr is None:
            continue
        sql_alchemy_filters.append(attr == value)
    return and_(True, *sql_alchemy_filters)
