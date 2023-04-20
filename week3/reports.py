from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.colors import PCMYKColor

def add_legend(draw_obj, chart):
    legend = Legend()
    legend.alignment = 'right'
    legend.x = 20
    legend.y = 30
    legend.colorNamePairs = Auto(obj=chart)
    draw_obj.add(legend)


def pie_chart_with_legend(data):
    car_sales = {}
    data = data[:20]
    for car, sales in data:
        if car in car_sales:
            car_sales[car] += sales
        else:
            car_sales[car] = sales

    drawing = Drawing(width=400, height=250)
    pie = Pie()
    pie.sideLabels = True
    pie.x = 150
    pie.y = 65
    pie.width = 200
    pie.height = 250


    pie.data = list(sorted(car_sales.values(),  reverse=True))
    # add a popout to the slice with the most sales
    index_of_max = pie.data.index(max(pie.data))

    pie.slices[index_of_max].popout = 10

    drawing.add(pie)

    pie.labels = [car_name for car_name in car_sales.keys()]

    add_legend(drawing, pie)
    return drawing


def bar_chart(data):
    # sort the data by sales and get the top 10
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)[:10]

    # create the chart
    drawing = Drawing(width=400, height=250)
    chart = VerticalBarChart()
    chart.width = 380
    chart.height = 200
    chart.x = 10
    chart.y = 30
    chart.data = [[sales for car, sales in sorted_data]]
    chart.categoryAxis.categoryNames = [car for car, sales in sorted_data]
    chart.categoryAxis.labels.angle = 45  # rotate the labels by 45 degrees
    chart.categoryAxis.labels.dy = -30

    chart.bars[0].fillColor   = PCMYKColor(100,90,0,0,alpha=85)
    
    # add the chart and axis labels
    drawing.add(chart)
    return drawing



def generate(filename, title, additional_info, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph("<br/>".join(additional_info), styles["BodyText"])

    # Create data for the pie chart
    total_sales = [(i[1].split('(')[0],i[3]) for i in table_data[1:]]  
    # print("==>> total_sales: ", total_sales)
    pie_title = Paragraph("Pie plot for a sublist of the data", styles["h2"])
    # Group the inner lists by car name
    chart = pie_chart_with_legend(total_sales)
    bar_title = Paragraph("Top 10 best selling cars", styles["h2"])
    bar = bar_chart(total_sales)


    table_style = [
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ]
    table_title = Paragraph("Sorted table for the maximum sales", styles["h2"])
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1, 50)

    report.build([
        report_title,
        empty_line,
        report_info,
        empty_line,
        pie_title,
        empty_line,
        empty_line,
        Image(chart),
        Spacer(1, 100),
        bar_title,
        Image(bar),
        empty_line,
        table_title,
        report_table
    ])
