import home
import tour
import user
from .settings import project

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.show_home_list,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = home.home_app)

tour.tour_app.add_url_rule(
    rule = "/tour",
    view_func = tour.show_tour,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = tour.tour_app)

user.user_app.add_url_rule(
    rule = "/user",
    view_func = user.show_user_app,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = user.user_app)