import os
import logging
import yaml

# Init common environment variables
environment_variables = {
    "basedir": os.path.abspath(os.path.dirname(__file__)),
    "config_dir": os.path.join(os.path.abspath(os.path.dirname(__file__)), "configs"),
    "icon_dir": os.path.join(os.path.abspath(os.path.dirname(__file__)), "icons"),
    "port": os.environ.get("PORT", "8080"),
    "debug": os.environ.get("DEBUG", False),
    "app_title": os.environ.get("TITLE", "AppBoard"),
    "app_heading": os.environ.get("HEADLINE", "AppBoard Applications"),
    "loglevel": os.environ.get("LOG_LEVEL", "INFO"),
    "prefix": os.environ.get("BASE_URL", ""),
}

# Init logger
# logging.basicConfig(format="[%(levelname)s]\t%(message)s", level=logging.INFO)
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=getattr(logging, environment_variables["loglevel"].upper(), logging.INFO),
)
logging.getLogger("werkzeug").disabled = True
logger = logging.getLogger()


def loadConfig():
    configFile = os.path.join(environment_variables["config_dir"], "config.yaml")

    if os.path.exists(configFile):
        with open(configFile) as f:
            config = yaml.safe_load(f)
        return config["categories"]
    else:
        logger.error("Config file does not exist")
        return ""
