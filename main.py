import argparse
import json
import logging
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
    asi_system = ASIMainControlLoop(config)
    asi_system.initialize_system()

    while True:
        input_data = asi_system.get_input()
        processed_input = asi_system.process_input(input_data)
        decision = asi_system.make_decision(processed_input)
        asi_system.execute_action(decision)

if __name__ == "__main__":
    main()
