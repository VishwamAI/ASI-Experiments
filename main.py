import argparse
import json
import logging
import sys
import os

# Ensure the current directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import ASIMainControlLoop

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def main():
    parser = argparse.ArgumentParser(description="Run the ASI system.")
    parser.add_argument('--config', type=str, default='config.json', help='Path to the configuration file')
    parser.add_argument('--log', type=str, default='asi.log', help='Path to the log file')
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Load configuration
    config = load_config(args.config)
    logging.info("Configuration loaded: %s", config)

    # Initialize and run the ASI system
    asi_system = ASIMainControlLoop()
    asi_system.initialize_system()

    try:
        while True:
            logging.info("Entering main loop iteration.")
            input_data = asi_system.get_input()
            processed_input = asi_system.process_input(input_data)
            decision = asi_system.make_decision()
            asi_system.execute_action(decision)

            # Check for environment variable to break the loop during testing
            if os.getenv('ASI_TEST_BREAK_LOOP') == '1':
                logging.info("Breaking loop for testing purposes.")
                break
    except KeyboardInterrupt:
        logging.info("ASI system interrupted and shutting down gracefully.")
    finally:
        logging.info("Exiting main function.")

if __name__ == "__main__":
    main()
