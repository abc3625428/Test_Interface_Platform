from flask import Flask,render_template
from setting.default import DefaultConfig
import log

from au import create_app

app = create_app(DefaultConfig, enable_config_file=True)






if __name__ == '__main__':

    app.run(debug=True)