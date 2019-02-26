from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/accounts/login')
def dashboard(request):
	return render(request, 'temp.html')

def json():
	line_chart_json = LineChartJSONView.as_view()
	return line_chart_json
