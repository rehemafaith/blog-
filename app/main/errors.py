from flask import render_template
from .  import main 

@main.app_errorhandler(404)
def four_Ow_four(error):
  '''
  Function to render thr 404 error page
  '''
  return render_template('fourOwfour.html'),404