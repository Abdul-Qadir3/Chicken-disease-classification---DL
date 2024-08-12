#Importing Required Libraries
import os # Used for interacting with the operating system for paths
import sys # Provides access to system-specific parameters and functions
import logging # Used to create and configure log messages, which are useful for debugging and monitoring the application.

# Define the Logging Setup
# logging_str: This string defines the format of the log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory and file path for logging
log_dir = "logs" #Defines the directory where log files will be stored
log_filepath = os.path.join(log_dir, "running_logs.log") #Combines the directory path and log file name to create the full path to the log file.
os.makedirs(log_dir, exist_ok=True) #Creates the logs directory if it doesn't already exist.
# The exist_ok=True parameter prevents an error if the directory already exists.

# Configuring Logging
# Basic configuration for logging
logging.basicConfig( 
    level=logging.INFO,#Sets the logging level to INFO, meaning it will capture all messages at this level and above 
    format=logging_str,#Applies the log message format defined earlier.
    handlers=[#Specifies where the log messages should be directed
        logging.FileHandler(log_filepath),  #Writes log messages to the specified log file
        logging.StreamHandler(sys.stdout)   #Outputs log messages to the console
    ]
)

# Create a logger object
# logger: This creates a logger object named "cnnClassifierlogger". 
# The logger object is used to log messages throughout the application.
logger = logging.getLogger("cnnClassifierlogger")