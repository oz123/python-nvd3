from nvd3 import lineChart, cumulativeLineChart
import random
import datetime
import time


def create_cumulativeLineChart():
    start_time = int(time.mktime(datetime.datetime(
        2012, 6, 1).timetuple()) * 1000)
    nb_element = 100

    type = "f"
    chart = cumulativeLineChart(name=type, height=350, x_is_date=True)
    chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

    xdata = list(range(nb_element))
    xdata = [start_time + x * 1000000000 for x in xdata]
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = [x * 2 for x in ydata]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " Calls"}}
    chart.add_serie(name="Count", y=ydata, x=xdata, extra=extra_serie)
    extra_serie = {"tooltip": {"y_start": "", "y_end": " Min"}}
    chart.add_serie(name="Duration", y=ydata2, x=xdata, extra=extra_serie)

    return chart


def create_line_chart():
    name = "Chart with spaces"
    chart = lineChart(name=name, date=True, height=350)
    chart.buildhtml()
    chart.header_js   # set when calling NVD3.__init__
    chart.header_css  # set when calling NVD3.__init__
    return chart


def test_line_chart():
    chart = create_line_chart()

    assert chart.width == u''
    assert chart.height == u'350'
    # names are slugified ...
    assert chart.name == u'chart_with_spaces'


def test_cumulativeLineChart():
    chart = create_cumulativeLineChart()

    assert chart.width == u''
    assert chart.height == u'350'
    # names are slugified ...
    assert chart.name == u'f'
