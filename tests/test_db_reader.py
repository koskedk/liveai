import json

from loguru import logger

from tasks.db_reader import DBReader

rdr=DBReader()

def test_get_connection():
    cn= rdr.get_connection();
    assert True

def test_get_schema():
    scm= rdr.get_schema("vwsales");
    assert scm is not None
    logger.info(json.dumps(scm,indent=4))

def test_get_data():
    data= rdr.get_data("select * from vwsales");
    assert data is not None
    for d in data:
        logger.info(f"{d['ProductKey']},	{d['EnglishProductName']},	{d['ModelName']},	{d['SalesAmount']},	{d['TaxAmt']},	{d['OrderDate']},	{d['CalendarQuarter']},	{d['CalendarYear']},	{d['MonthNumberOfYear']},	{d['EnglishMonthName']}")