from nvd3 import lineChart


def create_line_chart():
    name = "Chart with spaces"
    chart = lineChart(name=name, date=True, height=350)
    chart.buildhtml()
    
    chart.header_js  # set when calling NVD3.__init__  
    chart.header_css # set when calling NVD3.__init__  
    return chart


def test_line_chart():
    chart = create_line_chart()

    assert chart.width == u''
    assert chart.height == u'350'
    # names are slugified ...
    assert chart.name == u'chart_with_spaces'


