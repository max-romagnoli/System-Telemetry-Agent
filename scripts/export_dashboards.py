import os
from dotenv import load_dotenv
import requests
import json
import time

load_dotenv()

grafana_api_key = os.getenv('GRAFANA_SYNC_API')
grafana_url = os.getenv('GRAFANA_LOCAL_API_URI')

dashboards_directory = "../grafana/conf/provisioning/dashboards"


def fetch_dashboards(api_key, grafana_url):
    """
    Sends a request to Grafana API and returns a list of dashboards.
    """
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(f'{grafana_url}/search', headers=headers)
    return response.json()


def fetch_dashboard_details(api_key, grafana_url, dashboard_uid):
    """
    Sends a request to Grafana API and returns JSON of a specific dashboard.
    """
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.get(f'{grafana_url}/dashboards/uid/{dashboard_uid}', headers=headers)
    return response.json()


def files_are_different(existing_file, new_data):
    """
    Check if any updates have been made in a given dashboard. 
    """
    if os.path.exists(existing_file):
        with open(existing_file, 'r') as file:
            existing_data = json.load(file)
        
        existing_data.pop('version', None)
        new_data.pop('version', None)
        
        return existing_data != new_data
    else: # file does not exist: create new dashboard
        return True


def sync_json_files(dashboard_details, file_path):
    """
    Writes new changes in ../grafana/conf/provisioning/dashboards
    """
    dashboard_data = dashboard_details.get('dashboard', {})
    if files_are_different(file_path, dashboard_data):
        with open(file_path, 'w') as file:
            json.dump(dashboard_data, file, indent=4)
            print(f"Dashboard '{file_path}' updated with new changes.")


def export_dashboards():
    """
    Fetches dashboards from Grafana UI and iterates over them syncing new changes.
    """    
    dashboards = fetch_dashboards(grafana_api_key, grafana_url)

    for dashboard in dashboards:
        dashboard_title = dashboard['title']
        dashboard_uid = dashboard['uid']
        dashboard_details = fetch_dashboard_details(grafana_api_key, grafana_url, dashboard_uid)
        file_path = f"{dashboards_directory}/{dashboard_title}.json"
        sync_json_files(dashboard_details, file_path)


def main():
    
    if grafana_api_key is None:
        raise ValueError("No Grafana API Key found. Please check your .env file.")
    
    print("Syncing local JSON files to Grafana...")
    print("Refresh rate: 2s")
    
    while True:
        export_dashboards()
        time.sleep(2)


if __name__ == "__main__":
    main()