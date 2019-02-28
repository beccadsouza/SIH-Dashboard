# from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import numpy as np


class LineChartJSONView(BaseLineChartView):
	def get_labels(self):
		return ["January", "February", "March", "April", "May", "June", "July"]

	def get_providers(self):
		return ["Central", "Eastside", "Westside"]

	def get_data(self):
		return [list(np.random.rand(7,)),
				list(np.random.rand(7,)),
				list(np.random.rand(7,)),]

def json1():
	line_chart_json = LineChartJSONView.as_view()
	return line_chart_json

def json2():
	line_chart_json = LineChartJSONView.as_view()
	return line_chart_json

def json3():
	line_chart_json = LineChartJSONView.as_view()
	return line_chart_json
